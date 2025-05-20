import os
import shutil
from sklearn.model_selection import StratifiedShuffleSplit
from src.utils import get_frames, store_frames

def prepare_dataset(
    view="A4C",                         # or "A2C"
    input_dir="./data",
    output_dir="./data",
    jpg_base_name=None,
    n_frames=15,
    test_size=0.2,
    val_size=0.5,
    seed=0
):
    assert view in ["A4C", "A2C"], "View must be 'A4C' or 'A2C'"

    if jpg_base_name is None:
        jpg_base_name = f"{view}_jpg"

    print(f"🔄 Preparing {view} dataset...")

    path2videos = os.path.join(input_dir, view)
    videos, labels = [], []

    for root, _, files in os.walk(path2videos):
        for file in files:
            if file.endswith(".avi"):
                videos.append(os.path.join(root, file))
                labels.append(0 if "n" in file.lower() else 1)

    sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train_idx, test_idx = next(sss.split(videos, labels))
    train_videos = [videos[i] for i in train_idx]
    test_videos = [videos[i] for i in test_idx]
    test_labels = [labels[i] for i in test_idx]

    sss_val = StratifiedShuffleSplit(n_splits=1, test_size=val_size, random_state=seed)
    val_idx, final_test_idx = next(sss_val.split(test_videos, test_labels))
    val_videos = [test_videos[i] for i in val_idx]
    final_test_videos = [test_videos[i] for i in final_test_idx]

    for split in ["training", "validation", "test"]:
        os.makedirs(os.path.join(output_dir, f"{view}_{split}"), exist_ok=True)

    def move(videos, dest):
        for video in videos:
            shutil.copy(video, os.path.join(dest, os.path.basename(video)))

    move(train_videos, os.path.join(output_dir, f"{view}_training"))
    move(val_videos, os.path.join(output_dir, f"{view}_validation"))
    move(final_test_videos, os.path.join(output_dir, f"{view}_test"))

    # Extract and store frames
    for split in ["training", "validation", "test"]:
        folder = os.path.join(output_dir, f"{view}_{split}")
        for video in os.listdir(folder):
            video_path = os.path.join(folder, video)
            frames, _ = get_frames(video_path, n_frames=n_frames)
            frame_folder = video_path.replace(view, jpg_base_name).replace(".avi", "")
            os.makedirs(frame_folder, exist_ok=True)
            store_frames(frames, frame_folder)

    print(f" {view} preprocessing complete.")

