namespace Coding.SOLID
{
    internal class BirdHandler
    {
        private BirdProducer _birdProducer;

        public BirdHandler()
        {
            _birdProducer = new BirdProducer();
        }

        public void DoBirdAction()
        {
            Sparrow sparrow = this._birdProducer.ProduceBird("Sparrow") as Sparrow;
            Pinguin pinguin = this._birdProducer.ProduceBird("Pinguin") as Pinguin;

            this.HandleBirdMoves(sparrow);
            this.HandleBirdMoves(pinguin);

            this.HandleBirdMultiplies(sparrow);
            this.HandleBirdMultiplies(pinguin);

            this.HandleBirdGrowsAChild(sparrow);
            this.HandleBirdGrowsAChild(pinguin);
        }

        public void HandleBirdMultiplies(IBird bird)
        {
            bird.SearchForSpause();
            bird.Sing();
            bird.Dance();
        }

        public void HandleBirdMoves(IBird bird)
        {
            bird.Walk();
            bird.Fly();
        }

        public void HandleBirdGrowsAChild(IBird bird)
        {
            bird.ProduceEgg();
            bird.DefendEgg();
        }
    }
}