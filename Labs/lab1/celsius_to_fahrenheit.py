min_temperature = 0
max_temperature = 100
step = 10

# \t: A tab
print('Celsius\tFahrenheit')
# We let fahrenheit take the values
# - min_temperature
# - min_temperature + step
# - min_temperature + 2 * step
# - min_temperature + 3 * step
# ...
# up to the largest value smaller than max_temperature + step
for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = 9/5 * celsius + 32
    # {:10d}: fahrenheit as adecimal number in a field of width 10
    # {:7.d}:   celsius as a decimal number in a field of width 7
    print('{:7d}\t{:10.d}'.format(celsius, fahrenheit))
    
