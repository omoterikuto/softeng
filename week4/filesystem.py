# ファイル filesystem.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from file import File
from directory import Directory
from countingobserver import CountingObserver


class FileSystem(ABC):
  _instance: Optional[FileSystem] = None

  @staticmethod
  def get_instance():
    # 唯一のインスタンスを(必要なら生成して)返す．
    # (ここに何らかの処理を記述する)
    if (FileSystem._instance == None):
      FileSystem._instance = _SimpleFileSystem()
    return FileSystem._instance

  @abstractmethod
  def create_directory(self, name: str) -> Directory:
    pass
  
  @abstractmethod
  def create_file(self, name: str) -> File:
    pass

# FileSystem クラスの定義の直後に追加する
class _SimpleFileSystem(FileSystem):
  def create_directory(self, name: str) -> Directory:
    return Directory(name)

  def create_file(self, name: str) -> File:
    return File(name)