import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class singletonDeck {
  
	private static singletonDeck instance = new singletonDeck();
  
	private singletonDeck() {}
    
	public static singletonDeck getInstance() {
		
		cards = new ArrayList<Card>( );

		// build the deck
		Suit[] suits = {Suit.SPADES, Suit.HEARTS, Suit.CLUBS, Suit.DIAMONDS}; {
			for(Suit suit: suits) {
				for(int i = 2; i <= 14; i++) {
					cards.add(new Card(suit, i));
				}
			}
		
			// shuffle it!
			Collections.shuffle(cards, new Random( ));
		}
		return instance;
	}
    
	public void print( ) {
		for(Card card: cards) {
			card.print( );
		}
	}

	private static List<Card> cards;
}

