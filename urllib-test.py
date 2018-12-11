#!/usr/bin/env python3

from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    
    story_words = []
    
    for story_line in story:
        line_words = story_line.decode('utf-8').split()
        print(line_words)
        for word in line_words:
            story_words.append(word)
    print(story_words)
    for word in story_words:
        print(word)
