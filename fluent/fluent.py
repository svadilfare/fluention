#!/usr/bin/env python3

from typing import Any, Dict
from functools import wraps
from .utils import parametrized
from dataclasses import dataclass


@dataclass
class FluentAttribute:

    arg: str
    default_value: Any = None

    def __call__(self, value: Any = None):
        return value or self.default_value


def partial_function_builder(function, attribute, fluent_attributes, args, kwargs):
    def inner_function(value=None):
        new_kwargs = {**kwargs, attribute.arg: attribute(value)}
        print(args, kwargs, function.__code__.co_argcount)
        if len(args) + len(kwargs) + 1 == function.__code__.co_argcount:
            return function(*args, **new_kwargs)
        else:
            return PartialFunction(function, fluent_attributes, args, new_kwargs)

    return inner_function


class PartialFunction:
    def __init__(
        self, function, fluent_attributes: Dict[str, FluentAttribute], args, kwargs
    ):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.fluent_attributes = fluent_attributes
        print("__init__", self.function, self.fluent_attributes, self.args, self.kwargs)

    # TODO make type checker get it
    def __getattr__(self, name: str):
        # if f
        print(self.fluent_attributes, self.args, self.kwargs)
        try:
            return partial_function_builder(
                self.function,
                self.fluent_attributes[name],
                {k: v for k, v in self.fluent_attributes.items() if k != name},
                self.args,
                self.kwargs,
            )
        except KeyError:
            raise AttributeError(f"{name} is not an attribute of the function")


@parametrized
def fluent(func, arg: str, func_name: str = None, default_value: Any = None):
    """
    Creates a fluent function interface for the decorated function,
    and provides a helper method `func_name` to the returned object.
    """

    if not func_name:
        func_name = f"with_{arg}"

    print(func, func_name)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func, args, kwargs)
        if isinstance(func, PartialFunction):
            raise NotImplementedError()
        return PartialFunction(
            func, {func_name: FluentAttribute(arg, default_value)}, args, kwargs
        )

    return wrapper
