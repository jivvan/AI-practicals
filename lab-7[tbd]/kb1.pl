% All people who are graduating are happy
happy(X) :- graduating(X).

% Happy people smile
smile(X) :- happy(X).

% Ram is graduating
graduating(ram).
