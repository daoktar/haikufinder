#!/usr/bin/env python3

# Read the CMU pronounciation dictionary, count syllables (throwing away
# phoneme and stress information), and pickle the result.
#
# Requirements:
#     pip install nltk
#     python -m nltk.downloader cmudict
#
# Usage:
#     python haikufinder/cmudict/PickleCMUDict.py
#
# Produces ``cmudict.pickle`` next to this file.
#
# Copyright (c) 2009, Jonathan Feinberg <jdf@pobox.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. The name of the author may not be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os.path
import pickle

from nltk.corpus import cmudict

syllables: dict[str, int] = {}
for word, phonemes in cmudict.entries():
    word = word.upper()
    count = sum(1 for x in "".join(phonemes) if x.isdigit())
    if word in syllables:
        count = min(count, syllables[word])
    syllables[word] = count

out_path = os.path.join(os.path.dirname(__file__), "cmudict.pickle")
with open(out_path, "wb") as output:
    pickle.dump(syllables, output, protocol=4)

print(f"Wrote {len(syllables)} entries to {out_path}")
