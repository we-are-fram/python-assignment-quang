# -*- coding: utf-8 -*-
__all__ = ["AbsUsecase"]

from abc import ABC, abstractmethod


class AbsUsecase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
