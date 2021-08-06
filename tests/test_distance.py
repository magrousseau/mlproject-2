from mlproject.distance import haversine

def test_type_of_harversine():
    assert type(haversine(48.865070, 2.380009, 43.30370426862863, 3.3345627376988927)) == float