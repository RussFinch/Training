import java.sql.*;

public class UpdateTest {

	public static void main(String[] args) {
		
		try(
			
			Connection conn = DriverManager.getConnection(
				"jdbc:mysql://localhost:3306/library_db?useSSL=false", "radmin", "*****");
				
			Statement stmt = conn.createStatement();
		) {
		
			String strUpdate = "update books set qty = 0 where title = 'Introduction to Java'";
			System.out.println("The SQL query is: " + strUpdate);
			int countUpdated = stmt.executeUpdate(strUpdate);
			System.out.println(countUpdated + "records affected.");
		
			String strSelect = "Select * from books where title = 'Introduction to Java'";
			System.out.println("The SQL query is: " + strSelect);
			ResultSet rset = stmt.executeQuery(strSelect);
			while(rset.next()) {
			System.out.println(rset.getInt("id") + ", "
					+ rset.getString("author") + ", "
					+ rset.getString("title") + ", "
					+ rset.getInt("qty"));
			}
		
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}
}
