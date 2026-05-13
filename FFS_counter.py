#First use of python code on my website hopefully
from typing import *
from dataclasses import dataclass
from bs4 import BeautifulSoup

lst : TypeAlias = list[Union[int,str]]
fireflies : lst
def counter(n:int)->int:
    return n + 1
def str_split(firefly :str)->lst:
    fireflies = firefly.split()
    return fireflies


with open("home.html", "r") as bag:
    soup = BeautifulSoup(bag, "html.parser")

# <h5 id="count">FFS counter : 0</h5>
carton = soup.find("h5", id="count")

if carton is not None:
    gallon = carton.text.strip()

    fireflies = str_split(gallon)

    # Convert last element to int, increment it, and store it back
    fireflies[-1] = counter(int(fireflies[-1]))

    # Put the text back together
    carton.string = " ".join(map(str, fireflies))

    with open("home.html", "w") as bag:
        bag.write(str(soup))

    print("Counter updated successfully!")
else:
    print("Could not find the counter element.")