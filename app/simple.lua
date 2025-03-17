-- load the code from the file
-- redis-cli EVAL "$(cat simple.lua)" 0

local value = 10 + 1
return value
