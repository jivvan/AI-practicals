% If triangle is equilateral then it is isosceles
isosceles(ABC) :- equilateral(ABC).

% If triangle is isosceles then two sides AB & AC are equal
equal(ab, ac) :- isosceles(ABC).

% If AB & AC are equal then angle B & C are equal
equal(b , c) :- equal(ab, ac).

% ABC is an equilateral triangle
equilateral(ABC).