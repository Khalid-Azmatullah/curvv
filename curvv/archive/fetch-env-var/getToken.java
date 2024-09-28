public class Main {
    public static void main(String[] args) {
        String value = System.getenv("githubAPI");

        if (value != null) {
            System.out.println("The value of 'githubAPI' is: " + value);
        } else {
            System.out.println("The environment variable 'githubAPI' is not set.");
        }
    }
}
