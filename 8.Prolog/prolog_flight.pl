airport(torronto,50,60).
airport(madrid,75,45).
airport(london,75,80).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(malaga,50,30).
airport(paris,50,60).
airport(toulouse,40,30).

flight(torronto,madrid,iberia,800,480).
flight(torronto,madrid,united,950,540).
flight(torronto,madrid,airCanada,900,480).

flight(torronto,london,airCanada,500,360).
flight(torronto,london,united,650,420).

flight(london,barcelona,iberia,220,240).

flight(madrid,barcelona,iberia,120,65).
flight(madrid,barcelona,airCanada,100,60).

flight(madrid,valencia,iberia,40,50).

flight(madrid,malaga,iberia,80,120).

flight(malaga,valencia,iberia,80,120).

flight(valencia,barcelona,iberia,110,75).

flight(paris,toulouse,united,40,30).

is_flight(A,B) :-
	flight(A,B,C,D,E);flight(B,A,C,D,E).

is_cheap(A,B,C) :-
	(flight(A,B,C,Q,R);flight(B,A,C,Q,R)),Q<400.

tow_flights(A,B) :-
	((flight(A,X,C,Q,R),flight(X,B,C,Q,R));(flight(B,X,C,Q,R),flight(X,A,C,Q,R))).

prefered(A,B,C) :- 
	is_cheap(A,B,C);C=airCanada.

	
	
