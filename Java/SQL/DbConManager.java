import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class DbConManager {
	
	public static String dbLogin(String userName, String password) {

		String DbUrlString = "jdbc:mysql://win81-desktop.home.local:3306/ebookstore?useSSL=FALSE";
		System.out.println("\nDatabase Setup Commencing...");
		try (
				Connection conn = DriverManager.getConnection(DbUrlString, userName, password);
				Statement stmt = conn.createStatement();
				) {
			
				// Create books table if not already existing
				String sqlCreateTableBooks = "create table if not exists books "
						+ "(ID int, Title varchar(50), Author varchar(50), QTY int, primary key (ID))";
				int countCreation = stmt.executeUpdate(sqlCreateTableBooks);
				System.out.println((countCreation + 1) + ": Database table verified in setup.");
			
				//Insert test data
/*				String sqlInsertBooksData = "insert into books values "
						+ "(3001, 'A Tale of Two Cities', 'Charles Dickens', 30), "
						+ "(3002, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40), "
						+ "(3003, 'The Lion the Witch and the Wardrobe', 'C.S. Lewis', 25), "
						+ "(3004, 'The Lord of theRings', 'J.R.R Tolkien', 37), "
						+ "(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)";
					System.out.println("The SQL query is: " + sqlInsertBooksData);
					int countInserted = stmt.executeUpdate(sqlInsertBooksData);
					System.out.println(countInserted + " records inserted.\n");				
*/			
			} catch (SQLException ex) {
				ex.printStackTrace();
		}
		
		return "Database Setup complete.";
	}
}
