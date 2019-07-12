#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Kash Farhadi"

import cProfile
import pstats
import timeit
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats(10)
        return result
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    formatted_movies = []
    
    for item in movies:
        formatted_movies.append(item.split('\t')[1])

    seen = {}
    duplicates = []

    for movie in formatted_movies:
        if movie in seen:
            seen[movie] += 1
            duplicates.append(movie)
        else:
            seen[movie] = 1
    
    print(f"Found {len(duplicates)} duplicate movies:")
    
    # starter code
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)
    # return duplicates

@profile
def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit(),
    and computes a list of duplicate movie entries"""

    setup = 'from __main__ import find_duplicate_movies'
    repeat_num, run_num = 7, 5

    t = timeit.Timer("find_duplicate_movies('movies.txt')", setup)
    result = t.repeat(repeat= repeat_num, number=run_num)
    result= [number/float(run_num) for number in result]
    print(f"Best time across {repeat_num} repeats of {run_num} runs per")
    print(f"repeat: {min(result)} sec")
    return min(result)


def main():
    """Computes a list of duplicate movie entries"""
    timeit_helper()


    # result = find_duplicate_movies('movies.txt')
    # print('Found {} duplicate movies:'.format(len(result)))


    
if __name__ == '__main__':
    main()
