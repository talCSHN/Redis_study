-- load the code
-- $ redis-cli
-- 127.0.0.1:6379> script load 'return 100'
-- "22cd37f569ce84333afb93ba232d04d5aa6bb87a"
-- 127.0.0.1:6379> evalsha 22cd37f569ce84333afb93ba232d04d5aa6bb87a 0
-- (integer) 100

print("hello LUA world")
local value = 10 + 1

if value > 0 then
    print("value is positive") 
end

if value ~= 0 then
    print("value is non zero")
end

if value == 11 then
    print("value is 11")
end

local country = {"South Korea", "United States", "Japan"}
 -- start from index 1
print(country[1])
-- length function
print(#country) 
table.insert(country, 'China')

print(country[4])

for i, v in ipairs(country) do
    print(i, v)
end

for i=1, 5 do
    print(i)
end

local car = {color = 'white', name = "tesla"}
print(car['name'])

for k, v in pairs(car) do
    print(k, v)
end

