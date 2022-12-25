name = "Ayanaksha"
country = "Bharat"
para = f"I am {name} from {country}"
print(para)

para = "I am {1} from {0}"
print(para.format(country, name))

price = 2.499
txt = f"Buy 20 apples for only ${price:.2f}"
print(txt)