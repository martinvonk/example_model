from pathlib import Path

model_name = "MODEL_NAME"  # change model name
extent = [0.0, 1.0, 0.0, 1.0]  # change extent to model extent

paths = {
    "models": Path(__file__).parent.parent
    / "modeldata/models",  # change path to models folder
    "downloads": Path(__file__).parent.parent
    / "modeldata/downloads",  # set path to download folder
}
