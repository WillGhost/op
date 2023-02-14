local ttl = tonumber(ARGV[1])
local ts = tonumber(ARGV[2])
local edge = ts - ttl

redis.call('ZREMRANGEBYSCORE', KEYS[1], '-inf', edge)
redis.call('EXPIRE', KEYS[1], ttl)
redis.call('ZADD', KEYS[1], ts, ts)

return redis.call('ZCARD', KEYS[1])


<! -- #// redis-cli -h 127.0.0.1 -p 6379 --eval bb.lua mem , 120  1655698748.121
