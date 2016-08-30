<Query Kind="Program" />

void Main()
{
    var client = new GriffinClient("mdlrest");
    client.Stop();
    System.Threading.Thread.Sleep(1000);
    client.Start();
}

// Define other methods and classes here

class GriffinClient
{
    private const string Griffin_Server_URL = "http://138.91.191.144:5000/";
    private readonly string app;
    
    public GriffinClient(string app)
    {
        this.app = app;
    }
    
    public void Start()
    {
        string url = Griffin_Server_URL + "start/" + app;
        string response;
        GriffinClient.TryMakeRequest(url, out response);
    }
    
    public void Stop()
    {
        string url = Griffin_Server_URL + "stop/" + app;
        string response;
        GriffinClient.TryMakeRequest(url, out response);
    }
    
    private static bool TryMakeRequest(string url, out string responseStr)
    {
        var request = (System.Net.HttpWebRequest)System.Net.WebRequest.Create(new Uri(url));
        request.Method = "POST";
        Console.WriteLine("POST " + url);
        
        bool success = false;
        System.Net.WebResponse response;
        try
        {
            response = request.GetResponse();
            success = true;
        }
        catch (System.Net.WebException e)
        {
            Console.WriteLine(e);
            response = e.Response;
        }
        
        responseStr = new StreamReader(response.GetResponseStream()).ReadToEnd();
        Console.WriteLine(responseStr);
        return success;
    }
}