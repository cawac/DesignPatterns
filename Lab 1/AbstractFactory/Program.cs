using AbstractFactory;

ElfFactory elfFactory = new ElfFactory();
IMagician elfMage = elfFactory.CreateMagician();
SkeletonFactory skeletonFactory = new SkeletonFactory();
ISolider skeletonSolider = skeletonFactory.CreateSolider();
