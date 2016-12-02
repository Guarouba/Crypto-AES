#!/usr/bin/python

##########################
# cribdrag - An interactive crib dragging tool
# Daniel Crowley
# Copyright (C) 2013 Trustwave Holdings, Inc.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
##########################

import argparse
import re


def sxor(ctext, crib):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    results = []
    single_result = ''
    crib_len = len(crib)
    positions = len(ctext) - crib_len + 1
    for index in xrange(positions):
        single_result = ''
        for a, b in zip(ctext[index:index + crib_len], crib):
            single_result += chr(ord(a) ^ ord(b))
        results.append(single_result)
    return results


def print_linewrapped(text):
    line_width = 40
    text_len = len(text)
    for chunk in xrange(0, text_len, line_width):
        if chunk > text_len - line_width:
            print str(chunk) + chr(9) + text[chunk:]
        else:
            print str(chunk) + chr(9) + text[chunk:chunk + line_width]


ctext_len = len(ctext)
display_ctext = "_" * ctext_len
display_key = "_" * ctext_len

charset = '^[' + args.charset + ']+$'

response = ''

while response != 'end':
    print "Your message is currently:"
    print_linewrapped(display_ctext)
    print "Your key is currently:"
    print_linewrapped(display_key)

    crib = raw_input("Please enter your crib: ")
    crib_len = len(crib)

    results = sxor(ctext, crib)
    results_len = len(results)

    # Generate results
    for result_index in xrange(results_len):
        if re.search(charset, results[result_index]):
            print '*** ' + str(result_index) + ': "' + results[result_index] + '"'
        else:
            print str(result_index) + ': "' + results[result_index] + '"'

    response = raw_input("Enter the correct position, 'none' for no match, or 'end' to quit: ")

    # Replace part of the message or key
    try:
        response = int(response)
        if response < results_len:
            message_or_key = ''
            while message_or_key != 'message' and message_or_key != 'key':
                message_or_key = raw_input("Is this crib part of the message or key? Please enter 'message' or 'key': ")
                if message_or_key == 'message':
                    display_ctext = display_ctext[:response] + crib + display_ctext[response + crib_len:]
                    display_key = display_key[:response] + results[response] + display_key[response + crib_len:]
                elif message_or_key == 'key':
                    display_key = display_key[:response] + crib + display_key[response + crib_len:]
                    display_ctext = display_ctext[:response] + results[response] + display_ctext[response + crib_len:]
                else:
                    print 'Invalid response. Try again.'

    except ValueError:
        if response == 'end':
            print "Your message is: " + display_ctext
            print "Your key is: " + display_key
        elif response == 'none':
            print "No changes made."
        else:
            print "Invalid entry."
