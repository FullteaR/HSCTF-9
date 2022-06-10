import java.util.*;

public class Solve {

	public static void main(String[] args) {
		String match = "20_a1qti0]n/5f642kb\\2`qq4\\0q";
		String chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n\t";
		System.out.print("flag{");
		for(int i=0;i<28;i++){
			for(char c : chars.toCharArray()){
				StringBuilder flag = new StringBuilder();
				flag.append("****************************");
				flag.replace(i,i+1,String.valueOf(c));
				String convert = ATCSNightmare.linkDemLists(ATCSNightmare.recurses(ATCSNightmare.stackAttack(flag.toString()), "", 1));
				if(matchCount(convert, match)>0){
					System.out.print(c);
				}
			}
		}
		System.out.println("}");
	}

	private static int matchCount(final String str1, final String str2){
		assert str1.length() == str2.length();
		int retval = 0;
		for(int i=0;i<str1.length();i++){
			if(str1.charAt(i) == str2.charAt(i)){
				retval+=1;
			}
		}
		return retval;
	}
}
