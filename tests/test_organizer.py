"""Tests for the organizer module."""

import os
import tempfile
import shutil
from pathlib import Path

import pytest

from file_organizer.organizer import organize_files, create_directory_if_not_exists


def test_create_directory_if_not_exists():
    """Test creating a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, "test", "nested", "dir")
        create_directory_if_not_exists(test_dir)
        assert os.path.exists(test_dir)


def test_organize_files():
    """Test organizing files by extension."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        txt_file = os.path.join(tmpdir, "test.txt")
        jpg_file = os.path.join(tmpdir, "image.jpg")
        
        Path(txt_file).touch()
        Path(jpg_file).touch()
        
        # Define type mappings
        type_mappings = {
            'txt': os.path.join(tmpdir, 'text_files'),
            'jpg': os.path.join(tmpdir, 'image_files'),
            'other': os.path.join(tmpdir, 'other_files')
        }
        
        # Run organizer
        success, message = organize_files(tmpdir, type_mappings)
        
        # Assert success
        assert success is True
        assert os.path.exists(os.path.join(tmpdir, 'text_files', 'test.txt'))
        assert os.path.exists(os.path.join(tmpdir, 'image_files', 'image.jpg'))


def test_organize_files_with_unknown_extension():
    """Test organizing files with unknown extension."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test file with unknown extension
        unknown_file = os.path.join(tmpdir, "document.xyz")
        Path(unknown_file).touch()
        
        type_mappings = {
            'txt': os.path.join(tmpdir, 'text_files'),
            'other': os.path.join(tmpdir, 'other_files')
        }
        
        success, message = organize_files(tmpdir, type_mappings)
        
        assert success is True
        assert os.path.exists(os.path.join(tmpdir, 'other_files', 'document.xyz'))
