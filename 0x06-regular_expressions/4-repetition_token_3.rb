#!/usr/bin/env ruby
# RegEx that matches hb(any letter not 'o')n

puts ARGV[0].scan(/hb[^o]*n/).join
