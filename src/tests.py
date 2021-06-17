import pytest
import inference

def test_argument_length(capsys):
    '''This test checks the argument vector has only two arguments. Title and description'''
    inference.main(["--title", "Othello", '--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Correct number of arguments\n' in out

def test_arguments_present(capsys):
    '''This test checks whether the arguments in the argument vector are named title and description.'''
    inference.main(["--title", "Othello",'--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Title and description are present\n' in out

def test_title_length(capsys):
    '''This test checks whether the parameter in the title argument has correct length of characters and words.'''
    inference.main(["--title", "Othello",'--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Title argument has words and characters in range\n' in out

def test_description_length(capsys):
    '''This test checks whether the parameter in the description argument has correct length of characters and words.'''
    inference.main(["--title", "Othello",'--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Description argument has words and characters in range\n' in out

def test_specialchars_inputs(capsys):
    '''This test checks whether the parameter values for title and description have only alphanumeric characters.'''
    inference.main(["--title", "Othello",'--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Title and description have only alphanumeric characters\n' in out