#!/usr/bin/env ruby
# RegEx that matches a ten digit number

puts ARGV[0].scan(/^\d{10}$/).join
