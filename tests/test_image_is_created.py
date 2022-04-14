import os
import pytest
from app import main as module


def test_no_error_for_valid_image_extension():
    X_IMAGE = "MY_TEST_IMAGE.png"
    module.verify_image_extension(X_IMAGE)


def test_raises_runtime_error_for_invalid_image_ext():
    X_IMAGE = "MY_TEST_IMAGE.image"
    with pytest.raises(RuntimeError):
        module.verify_image_extension(X_IMAGE)


def test_flipped_append_to_output_filename():
    X_IMAGE = "MY_TEST_IMAGE.png"
    opImage = module.get_output_file_name(X_IMAGE)
    name, _ = os.path.splitext(opImage)
    assert name.endswith("flipped")


def test_image_is_created():
    pass