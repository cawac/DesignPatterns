namespace Coding.SOLID
{
    public class BirdProducer
    {
        public object ProduceBird(string birdType)
        {
            if (birdType == "Pinguin")
            {
                return new Pinguin();
            }
            if (birdType == "Sparrow")
            {
                return new Sparrow();
            }

            return new object();
        }


    }
}