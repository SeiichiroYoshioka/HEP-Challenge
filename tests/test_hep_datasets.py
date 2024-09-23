from ingestion_program.hep_datasets import Data

def test_get_train_set():
    data = Data("./sample_data/input_data")
    data.load_train_set()
    train_set = data.get_train_set()
    assert train_set is not None