#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ######################################################################
# Copyright (C) 2016-2017  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of Selinon project.
# ######################################################################
"""A Python class abstraction"""


class TaskClass(object):
    """
    Task's class abstraction
    """
    def __init__(self, class_name, import_path):
        self.class_name = class_name
        self.import_path = import_path
        self.tasks = []

    def task_of_class(self, task):
        """
        :param task: task to be checked
        :return: True if task is of this class
        """
        return self.class_name == task.class_name and self.import_path == task.import_path

    def add_task(self, task):
        """
        Register a task to this class

        :param task: task to be added
        """
        assert self.task_of_class(task)
        self.tasks.append(task)
