#!/usr/bin/env ruby

require 'rubygems'
require 'bundler/setup'

require 'active_support/all'
require 'twitter'

class GeeokiGomi
  # TODO: Web UI for manage Geeoki people accounts
  def accounts
    %w(tompng gliese035 hanachin_ kimihito_)
  end

  # TODO: Fix GOMI schedule
  def gomi_message(time = Time.now)
    case time.wday
    when 0 then '今日はゆっくり休みましょ'
    when 1 then '今日は燃えるゴミの日ですよ！'
    when 2 then '今日は燃やさないゴミの日！'
    when 3 then '今日は紙・布の日！'
    when 4 then '今日は燃えるゴミの日ですよ！'
    when 5 then '今日は缶・ビン・ペットボトルの日!'
    when 6 then 'ゴミはないけど、掃除しようぜ！'
    end
  end

  def message
    "#{accounts.map {|n| "@#{n}"}.join ' '} #{gomi_message}"
  end
end

Twitter.update GeeokiGomi.new.message
