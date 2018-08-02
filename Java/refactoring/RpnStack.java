class RpnStack {
	
  public static RpnStack top;
  public static RpnStack underneath;
  public double data;
  

  public RpnStack(double newData, RpnStack top) {	  
    this.data = newData;
    RpnStack.underneath = top;
  }
  
  public static void intoRpnStack(double newData) {
    RpnStack newNode = new RpnStack(newData, top);
	RpnStack.top = newNode;
  }
  
  public static double outOfRpnStack() {
	double topData = top.data;
	RpnStack.top = RpnStack.underneath;
	return topData;
  }
}