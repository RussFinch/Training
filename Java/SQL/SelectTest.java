import java.sql.*;

public class SelectTest {

	public static void main(String[] args) {
		
		try (
			
			Connection conn = DriverManager.getConnection(
					"jdbc:mysql://win81-desktop.home.local:3306/ebookstore?useSSL=false", "radmin", "L966fth!");
				
			Statement stmt = conn.createStatement();
		)	{
		
		String strSelect = "select title, qty from books";
		System.out.println("The SQL Query is: " + strSelect);
		System.out.println();
		
		ResultSet rset = stmt.executeQuery(strSelect);
		
		System.out.println("The records selected are:");
		int rowCount = 0;
		
		while(rset.next()) {
			String title = rset.getString("title");
			int qty = rset.getInt("qty");
			System.out.println(title + ", " + qty);
			++rowCount;
		}
		
		System.out.println("Total number of records = " + rowCount);
		
		} 
		
		catch(SQLException ex) {
			ex.printStackTrace();
		}
		
	}		
}
