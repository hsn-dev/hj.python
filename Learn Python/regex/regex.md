[RegEx Tutorial Website ](http://www.regular-expressions.info/)

---

## Regular Expression:

A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings,
using a specialized syntax held in a pattern. 

Regular expressions are widely used in UNIX world.

A regular expression “engine” is a piece of software that can process regular expressions, trying to match the pattern to the given string.

The Python module re provides full support for Perl-like regular expressions in Python.

---

## Literal Characters

- The most basic regular expression consists of a single literal character, such as a. 

- It matches the first occurrence of that character in the string. If the string is **Jack is a boy**.

- Note that regex engines are case sensitive by default. cat does not match Cat, unless you tell the regex engine to ignore differences in case.

---

## Special Characters | Meta Characters

Because we want to do more than simply search for literal pieces of text, we need to reserve certain characters for special use. 

There are 11 characters with special meanings:

1. backslash \
2. caret ^
3. dollar sign $
4. period or dot .
5. vertical bar or pipe symbol |
6. question mark ?
7. asterisk or star *
8. plus sign +
9. parenthesis ( )
10. square brackets [ ]
11. curly braces { }

If you want to use any of these characters as a literal in a regex, you need to escape them with a backslash.

If you want to match 1+1=2, the correct regex is 1\\+1=2. Otherwise, the plus sign has a special meaning.

---

## Character Set

- You can tell the regex engine to match only one out of several characters.

- Simply place the characters you want to match between square brackets [ ].

- A character class matches only a single character.

gr[ae]y does not match graay, graey or any such thing. 

The order of the characters inside a character class does not matter. The results are identical.

You can use a hyphen inside a character class to specify a range of characters. 

[0-9] matches a single digit between 0 and 9.

You can use more than one range. [a-zA-Z0-9]

---

## Negated Character Set

- Typing a caret ^ after the opening square bracket negates the character set.

- The result is that the character set matches any character that is not in the character set.

- It is important to remember that a negated character class still must match a character.

### PROBLEM 

Iraq is a country

q[^u] does not mean: “a q not followed by a u”.

It means: “a q followed by a character that is not a u”.

It does not match the q in the string Iraq.

It does match the q and the space after the q.

Indeed: the space becomes part of the overall match, because it is the “character that is not a u”

---

## Anchors

Thus far, we have learned about literal characters, character classes, and the dot.

Putting one of these in a regex tells the regex engine to try to match a single character.

- Anchors are a different breed.
- They do not match any character at all. 
- Instead, they match a position before, after, or between characters.

---

## Word Boundaries

- The metacharacter \b is an anchor like the caret and the dollar sign. 
- It matches at a position that is called a “word boundary”. 
- This match is zero-length.

There are three different positions that qualify as word boundaries:

1. Before the first character in the string, if the first character is a word character.
2. After the last character in the string, if the last character is a word character.
3. Between two characters in the string, where one is a word character and the other is not a word character.

[Word Boundary in Detail](http://www.regular-expressions.info/wordboundaries.html)

---
<br>

|  Metachar  |			             Meaning			    			|
-------------|-----------------------------------------------------------
|	 .	     | Any char except newline	 								|
|	\d		 | Digit (0-9)							     				|
|   \D       | Not a digit (0-9) 										|
|	\w		 | Word character (a-z, A-Z, 0-9, underscore)				|
|	\W		 | Not a word character										|
|	\s		 | Whitespace (space, tab, newline)							|
|   \S		 | Not a Whitespace											|
|	[ ]		 | Matches Characters in CharacterSet (brackets)	    	|
|	[^ ]	 | Matches Characters not in CharacterSet (brackets)	    |

<br>

|  Anchor    |			             Meaning			    			|
-------------|-----------------------------------------------------------
|	\b		 | Word boundary (space, \n, \t) before or after text		|
|	\B		 | Not having a word boundary				     		    |
|	^		 | Beginning of a string									|
|	$		 | End of a string					    					|

<br>

|  Quantifiers    |			             Meaning			    			|
------------------|----------------------------------------------------------
|	*		      | 0 or more		                                        |
|	+		      | 1 or more			     		                        |   
|	?		      | 0 or one								               	|
|	{3}		      | Exact number of time				    				|
|	{3,4}		  | Range Of Numbers (min, max)				   			    |

## Alteration
    Search for the literal text cat or dog, cat | dog
## Optional
    colou?r     [u is optional]
## Repitition
    [A-Z]+      one or more occurrunce
    [A-Z]*      0 or more occurrunce
## Grouping
    hsn.dev@gmail.(com|edu|net)

## Limiting Repitition

- There’s an additional quantifier that allows you to specify how many times a token can be repeated.
- The syntax is {min,max}, where min is zero or a positive integer number indicating the minimum number of matches
- max is an integer equal to or greater than min indicating the maximum number of matches.
- If the comma is present but max is omitted, the maximum number of matches is infinite.
- { 0, 1 } is the same as ? 
- { 0, } is the same as *
- { 1, } is the same as +
- Omitting both the comma and max tells the engine to repeat the token exactly min times.

    #### For example:
        You could use [1-9][0-9]{3} to match a number between 1000 and 9999