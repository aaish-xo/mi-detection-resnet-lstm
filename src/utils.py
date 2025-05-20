import os
import cv2

def get_frames(video_path, n_frames=15):
    """Extracts a fixed number of evenly spaced frames from a video."""
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames == 0:
        raise ValueError(f"Video {video_path} has no frames.")

    frame_indices = [int(i * total_frames / n_frames) for i in range(n_frames)]
    frames = []
    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        if i in frame_indices:
            frames.append(frame)
    cap.release()
    return frames, total_frames

def store_frames(frames, out_folder):
    """Saves list of frames as JPGs to the output folder."""
    for idx, frame in enumerate(frames):
        frame_path = os.path.join(out_folder, f"frame{idx}.jpg")
        cv2.imwrite(frame_path, frame)
