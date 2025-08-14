from pathlib import Path

from shapely import LineString

model_name = "Haamstede"
extent = ([35_000.0, 48_000.0, 410_000.0, 419_000.0],)
cross_sections = (
    {
        "A": LineString([(35632.0, 411759.0), (47848.0, 416205.0)]),
        "B": LineString([(36318.0, 417329.0), (39396.0, 408872.0)]),
        "C": LineString([(37030.0, 412170.0), (39150.0, 413160.0)]),
    },
)
tmin = "2013"
tmax = "2024"
paths = {
    "models": Path(__file__).parent.parent / "modeldata/models",
    "downloads": Path(__file__).parent.parent / "modeldata/downloads",
}
