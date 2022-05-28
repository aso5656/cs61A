"""Typing test implementation"""

from subprocess import call
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    selected_paragraph = list(filter(select, paragraphs))

    return selected_paragraph[k] if len(selected_paragraph) > k else ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def topic_contains(paragraph):
        paragraph = split(remove_punctuation(lower(paragraph)))
        for each_topic in topic:
            if each_topic in paragraph:
                return True
        return False

    return topic_contains
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    total = len(typed_words)

    def func(typed_words, reference_words, n):

        if len(typed_words) * len(reference_words) == 0:
            return 0.0 if total == 0 else n / total * 100

        elif typed_words[0] == reference_words[0]:
            n += 1

        return func(typed_words[1:], reference_words[1:], n)

    return func(typed_words, reference_words, 0)

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word

    else:
        #pass each word into diff_function, return word from valid_words with min diff
        word_with_min_diff = min(valid_words, key=lambda word: diff_function(user_word, word, limit))

        if diff_function(user_word, word_with_min_diff, limit) > limit:
            return user_word
        else:
            return word_with_min_diff


    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """

    # BEGIN PROBLEM 6

    if limit < 0:
        return 0
    
    if len(start) * len(goal) == 0:
            return len(start)+ len(goal)
    
    elif start[0] != goal[0]:
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)

    else:
        return shifty_shifts(start[1:], goal[1:], limit)

    # def func(start, goal, n):
    #     if len(start) * len(goal) == 0:
    #         return n + len(start)+ len(goal)

    #     else:
    #         if start[0] != goal[0]:
    #             #check number of characters that must change
    #             if n == limit:
    #             #if already 'limit' , 
    #             #stop and return any number larger than limit
    #                 return n+1
    #             else:
    #             #next change
    #                 return func(start[1:], goal[1:], n+1)
    #         else:
    #             return func(start[1:], goal[1:], n)

    # return func(start, goal, 0)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0:
        return 0

    if len(start)*len(goal) ==0:
        return abs(len(start)-len(goal))
    
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:],goal[1:],limit)
    else:
        limit -= 1
        #print("DEBUG", limit)
        add_diff = pawssible_patches(start,goal[1:],limit)
        remove_diff = pawssible_patches(start[1:],goal,limit)
        substitute_diff = pawssible_patches(start[1:],goal[1:],limit)
        return 1 + min(add_diff,remove_diff,substitute_diff)


    
    # def func(start,goal,add_diff,remove_diff,substitute_diff):

    #     n = add_diff+remove_diff+substitute_diff

    #     if len(start) * len(goal) == 0:  # Fill in the condition
    #         # BEGIN
    #         return n + len(start)+ len(goal)
    #         # END

    #     elif start[0] != goal[0]:  # Feel free to remove or add additional cases
    #         # BEGIN
    #         #check number of edits
    #         if n == limit:
    #             #if already edit limit times, 
    #             #stop and return any number larger than limit
    #             return n+1
    #         else:
    #             #add goal[0] to head         
    #             add = func(start,goal[1:],add_diff+1,remove_diff,substitute_diff)
    #             #remove start[0]
    #             remove = func(start[1:],goal,add_diff,remove_diff+1,substitute_diff)
    #             #repalce start[0] with goal[0]
    #             sub = func(start[1:],goal[1:],add_diff,remove_diff,substitute_diff+1)

    #             return min(add, remove, sub)
    #             # END

    #     else:
    #         return func(start[1:],goal[1:],add_diff,remove_diff,substitute_diff)
           
    #         # BEGIN
    #         "*** YOUR CODE HERE ***"
    #         # END
    # return func(start,goal,0,0,0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    d = {'id': user_id,'progress':0}

    corrcect_num = 0

    for index,value in enumerate(typed):

        if value == prompt[index]:
            corrcect_num +=1
        else:
            break

    d['progress'] = corrcect_num/len(prompt)
    send(d)
    return d['progress'] 


    #send({"id":user_id,"progress":ratio})

    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    #[[1, 3, 5], [2, 5, 6]]->zip([3,5],[1,3])->[3-1,5-3]
    time_list = lambda li:[x-y for x,y in zip(li[1:],li[:-1])]
    times = [time_list(li) for li in times_per_player]

    return game(words,times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(
        all_times(game)))  # contains an *index* for each player
    word_indices = range(len(
        all_words(game)))  # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    results = [[] for player_indice in player_indices]

    for word_indice in word_indices:
        fastest_player,fastest_time,timestamp = 0,0,0

        for player_indice in player_indices:
            word_time = time(game,player_indice,word_indice)
            time_to_word = sum(all_times(game)[player_indice][:word_indice+1])

            if word_time > fastest_time and fastest_time != 0:
                continue
            elif word_time == fastest_time:
                if time_to_word > timestamp:
                    continue
            else:
                fastest_player = player_indice
                fastest_time = word_time
                timestamp = time_to_word

        results[fastest_player].append(word_at(game,word_indice))

    return results

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str
                for w in words]), 'words should be a list of strings'
    assert all([type(t) == list
                for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times
                for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words)
                for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print(
            'If you only type part of it, you will be scored only on that part.\n'
        )
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)