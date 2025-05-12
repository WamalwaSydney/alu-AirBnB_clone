#!/usr/bin/python3
"""Models package initializer."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
