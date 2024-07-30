using System;
using MySql.Data.MySqlClient;

class Program
{
    static void Main(string[] args)
    {
        string connectionString = "server=localhost;user=root;database=myorders;port=3306;password=Nikunj@26";
        using (var connection = new MySqlConnection(connectionString))
        {
            try
            {
                connection.Open();
                string query = "SELECT * FROM Orders";
                MySqlCommand cmd = new MySqlCommand(query, connection);
                MySqlDataReader reader = cmd.ExecuteReader();

                while (reader.Read())
                {
                    Console.WriteLine($"OrderID: {reader["OrderID"]}, CustomerNumber: {reader["CustomerNumber"]}, ItemNumber: {reader["ItemNumber"]}, Quantity: {reader["Quantity"]}, Price: {reader["Price"]}, OrderDate: {reader["OrderDate"]}");
                }
                reader.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
