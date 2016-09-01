<Query Kind="Program" />

void Main()
{
    var client = new GriffinClient("mdlrest");
//    var client = new GriffinClient("myapp-group");

    client.Stop();
    System.Threading.Thread.Sleep(1000);

    client.Start("latest", 5); // mdlrest:latest

//    client.Start("1", 2);     //myapp:1
//    client.Upgrade("2", 2);   //myapp:2
//    client.Upgrade("2", 4);   //myapp:2
//    client.Upgrade("bad", 4); //myapp:bad
}

// Define other methods and classes here

class GriffinClient
{
    private const string Griffin_Server_URL = "http://138.91.191.144:5000/";
	private const string POST = "POST";
	private const string PUT = "PUT";
    private readonly string app;
    
    public GriffinClient(string app)
    {
        this.app = app;
    }

    public void Start(string ver, int scale)
    {
        this.Start(ver, scale, false);
    }

    public void Upgrade(string ver, int scale)
    {
        this.Start(ver, scale, true);
    }

    public void Stop()
    {
        string url = Griffin_Server_URL + "stop/" + app + "?force=true";
        string response;
        GriffinClient.TryMakeRequest(url, POST, out response);
    }
    
    private void Start(string ver, int scale, bool upgrade)
    {
        string url = Griffin_Server_URL + "start/" + app + "/" + ver + "/" + scale;
        string response;
        GriffinClient.TryMakeRequest(url, upgrade ? PUT : POST, out response);
    }
    
    private static bool TryMakeRequest(string url, string method, out string responseStr)
    {
        var request = (System.Net.HttpWebRequest)System.Net.WebRequest.Create(new Uri(url));
        request.Method = method;
        Console.WriteLine(method + " " + url);
        
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