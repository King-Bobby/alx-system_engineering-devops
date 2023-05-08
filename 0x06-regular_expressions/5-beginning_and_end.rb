#!/usr/bin/env ruby
# RegEx that matches a string that starts with h, then any single character,
# then ends with n eg(hbn, h8n, h0n, han, h%n)

puts ARGV[0].scan(/^h.n$/).join
