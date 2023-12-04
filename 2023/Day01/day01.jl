A = read("input.txt", String)
lines = split(A, "\n")


digits = [string(x) for x in 1:9]

function get_first_digit(line)
    for l in line
        if l in digits
            return l
        end
    end
end

# Part 1
function solution1()
    result1 = 0
    for line in lines
        letters = split(line, "")
        num = string(get_first_digit(letters), get_first_digit(reverse(letters)))
        result1 = result1 + parse(Int64, num)
    end
    print("Solution 1\n", result1, "\n")
    return result1
end



## Part 2
number_names = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine"]

function replace_front(line)
    indices = [isnothing(findfirst(x, line)) ?  100 : findfirst(x, line)[1] for x in number_names]
    ind_min = minimum(indices)
    newline = deepcopy(line)
    if ind_min < 100
        index = argmin(indices)[1]
        newline = replace(newline, number_names[index] => digits[index], count =1)
    end
    return split(newline, "")
end

function replace_back(line)
    newline = reverse(line)
    indices = [isnothing(findfirst(reverse(x), newline)) ?  100 : findfirst(reverse(x), newline)[1] for x in number_names]
    ind_min = minimum(indices)
    if ind_min < 100
        index = argmin(indices)[1]
        newline = replace(newline, reverse(number_names[index]) => digits[index], count =1)
    end
    return split(newline, "")
end


function solution2()
    result2 = 0
    for line in lines
        num = string(get_first_digit(replace_front(line)), get_first_digit(replace_back(line)))
        result2 = result2 + parse(Int64, num)
    end
    print("Solution 2\n", result2, "\n")
    return result2
end

result1 = solution1()
result2 = solution2()


