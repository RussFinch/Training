import java.sql.*;

public class InsertTest {

	public static void main(String[] args) {

		try (
			Connection conn = DriverManager.getConnection(
				"jdbc:mysql://localhost:3306/library_db?useSSL=false", "radmin", "L966fth!");
			
			Statement stmt = conn.createStatement();
		) {
		
			String sqlDelete = "delete from books where id>8000";
			System.out.println("The SQL Query is: " + sqlDelete);
			int countDeleted = stmt.executeUpdate(sqlDelete);
			System.out.println(countDeleted + " records inserted.\n");
			
			String sqlInsert = "insert into books values "
				+ "(8001, 'Java ABC', 'Kevin Jones', 3), "
				+ "(8002, 'Java XYZ', 'Kevin Jones', 5)";
			System.out.println("The SQL query is: " + sqlInsert);
			int countInserted = stmt.executeUpdate(sqlInsert);
			System.out.println(countInserted + " records inserted.\n");

			String strSelect = "select * from books";
			System.out.println("The SQL query is: " + strSelect);
			ResultSet rset = stmt.executeQuery(strSelect);
					// Move the cursor to the next row
			while (rset.next()) {
				System.out.println(rset.getInt("id") + ", "
						+ rset.getString("author") + ", "
						+ rset.getString("title") + ", "
						+ rset.getInt("qty"));
			}
			
		} catch (SQLException ex) {
			ex.printStackTrace();
		}
	}
}