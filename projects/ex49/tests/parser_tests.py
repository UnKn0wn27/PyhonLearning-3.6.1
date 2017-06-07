from nose.tools import *
from ex49 import parser
from ex49 import lexicon

def test_sentence_obj():
    s = parser.Sentence(('number', 1),('noun', 'bear'), ('verb','go'), ('direction', 'north'))
    assert_equal(s.number, 1)
    assert_equal(s.subject, 'bear')
    assert_equal(s.verb, 'go')
    assert_equal(s.object, 'north')
    assert_equal(s.make_tuple(), (1, 'bear', 'go', 'north'))

def test_peek():
    word = 'one'
    scaner = lexicon.scan('bear')

    assert_equal(parser.peek(word), 'o')
    assert_equal(parser.peek(scaner), 'noun')
    assert_equal(parser.peek(None), None)

def test_match():
    words = ['one', 'two', 'three']
    scanner = lexicon.scan("bear go north")

    assert_equal(parser.match(words,'o'), 'one')
    assert_equal(parser.match(scanner,'noun'), ('noun','bear'))
    assert_equal(parser.match(scanner, None), None)
    assert_equal(parser.match(None, 'noun'), None)
    assert_equal(parser.match(None, None), None)

def test_skip():
    scanner = lexicon.scan("north bear go")
    assert_equal(scanner, [('direction', 'north'), ('noun', 'bear'), ('verb', 'go')])
    assert_equal(parser.skip(scanner, 'direction'), None)
    assert_equal(scanner, [('noun', 'bear'), ('verb', 'go')])

def test_parse_number():
    scanner = lexicon.scan("the 1 bear")
    assert_equal(scanner, [('stop', 'the'), ('number', 1), ('noun', 'bear')])
    assert_equal(parser.parse_number(scanner), ('number', 1))
    assert_raises(parser.ParserError, parser.parse_number, scanner)

def test_parse_verb():
    scanner = lexicon.scan("the in go north bear")
    assert_equal(scanner, [('stop', 'the'), ('stop', 'in'),
                           ('verb', 'go'), ('direction', 'north'), ('noun', 'bear')])
    assert_equal(parser.parse_verb(scanner), ('verb', 'go'))
    assert_equal(scanner, [('direction', 'north'), ('noun', 'bear')])
    assert_raises(parser.ParserError, parser.parse_verb, scanner)

def test_parse_object():
    scanner = lexicon.scan("the north bear")
    assert_equal(scanner, [('stop', 'the'), ('direction', 'north'), ('noun', 'bear')])
    assert_equal(parser.parse_object(scanner), ('direction', 'north'))
    assert_equal(scanner, [('noun', 'bear')])

    scanner = lexicon.scan ("the bear north")
    assert_equal(scanner, [('stop', 'the'), ('noun', 'bear'), ('direction', 'north')])
    assert_equal(parser.parse_object(scanner), ('noun', 'bear'))
    assert_equal(scanner, [('direction', 'north')])

def test_parse_subject():
    scanner = lexicon.scan("the bear go")
    assert_equal(scanner, [('stop', 'the'), ('noun', 'bear'), ('verb', 'go')])
    assert_equal(parser.parse_subject(scanner), ('noun', 'bear'))
    assert_equal(scanner, [('verb', 'go')])

    scanner = lexicon.scan("the go bear")
    assert_equal(scanner, [('stop', 'the'), ('verb', 'go'), ('noun', 'bear')])
    assert_equal(parser.parse_subject(scanner), ('noun', 'player'))
    assert_equal(scanner, [('verb', 'go'), ('noun', 'bear')])

def test_parse_sentence():
    scanner = lexicon.scan("1 bear go north")
    s = parser.parse_sentence(scanner)
    assert_equal(s.make_tuple(), (1, 'bear', 'go', 'north'))
