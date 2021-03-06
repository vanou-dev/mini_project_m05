from HousePricesDatabase import HousePricesDatabase
from DataPreprocessing import DataPreprocessing
#from RFAlgorithm import RandomForestTraining
#from Analysis import Analysis

import nose.tools
import numpy as np


def test_HousePricesDatabase():
    """Test the limit case of the class HousePricesDatabase when all the parameters are given as input"""

    db_path = "./house-prices/house-prices.csv"

    # Nominal parameters:
    nominal = ["MS SubClass", "MS Zoning", "Street", "Alley", "Land Contour", "Lot Config", "Neighborhood",
               "Condition 1", "Condition 2", "Bldg Type", "House Style", "Roof Style", "Roof Matl", "Exterior 1st",
               "Exterior 2nd", "Mas Vnr Type", "Foundation", "Heating", "Central Air", "Garage Type", "Misc Feature",
               "Sale Type", "Sale Condition"]

    # Continuous parameters:
    continuous = ["Lot Frontage", "Lot Area", "Mas Vnr Area", "BsmtFin SF 1", "BsmtFin SF 2", "Bsmt Unf SF",
                  "Total Bsmt SF", "1st Flr SF", "2nd Flr SF", "Low Qual Fin SF", "Gr Liv Area", "Garage Area",
                  "Wood Deck SF", "Open Porch SF", "Enclosed Porch", "3Ssn Porch", "Screen Porch", "Pool Area",
                  "Misc Val"]

    # Ordinal parameters:
    ordinal = ["Lot Shape", "Utilities", "Land Slope", "Overall Qual", "Overall Cond", "Exter Qual", "Exter Cond",
               "Bsmt Qual", "Bsmt Cond", "Bsmt Exposure", "BsmtFin Type 1", "BsmtFin Type 2", "Heating QC",
               "Electrical",
               "Kitchen Qual", "Functional", "Fireplace Qu", "Garage Finish", "Garage Qual", "Garage Cond",
               "Paved Drive", "Pool QC", "Fence"]

    # Discrete parameters:
    discrete = ["Year Built", "Year Remod/Add", "Bsmt Full Bath", "Bsmt Half Bath", "Full Bath", "Half Bath",
                "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd", "Fireplaces", "Garage Yr Blt", "Garage Cars",
                "Mo Sold", "Yr Sold"]

    protocol = [0.8, 0.1, 0.1]

    house_price_db = HousePricesDatabase(db_path, continuous, discrete, ordinal, nominal, protocol)
    train_set, cv_set, test_set = house_price_db()

    # Test that there are 1492 samples in all the elements of the train set
    nose.tools.eq_(train_set[0].shape[0], 1492)
    nose.tools.eq_(train_set[0].shape[0], train_set[1].shape[0])
    nose.tools.eq_(train_set[0].shape[0], train_set[2].shape[0])
    # Test that there are 186 samples in all the elements of the cv set
    nose.tools.eq_(cv_set[0].shape[0], 186)
    nose.tools.eq_(cv_set[0].shape[0], cv_set[1].shape[0])
    nose.tools.eq_(cv_set[0].shape[0], cv_set[2].shape[0])
    # Test that there are 186 samples in all the elements of the test set
    nose.tools.eq_(test_set[0].shape[0], 187)
    nose.tools.eq_(test_set[0].shape[0], test_set[1].shape[0])
    nose.tools.eq_(test_set[0].shape[0], test_set[2].shape[0])

    # Test that there are 33 discrete/continuous params:
    nose.tools.eq_(train_set[0].shape[1], 33)
    nose.tools.eq_(cv_set[0].shape[1], 33)
    nose.tools.eq_(test_set[0].shape[1], 33)
    # Test that there are 46 categorical params:
    nose.tools.eq_(train_set[1].shape[1], 46)
    nose.tools.eq_(cv_set[1].shape[1], 46)
    nose.tools.eq_(test_set[1].shape[1], 46)

    # Verify that the same samples were used.
    nose.tools.eq_(np.sum(train_set[0]), 35786796.0)
    nose.tools.eq_(np.sum(train_set[2]), 276971674)
    nose.tools.eq_(np.sum(cv_set[0]), 4383366.0)
    nose.tools.eq_(np.sum(cv_set[2]), 33287207)
    nose.tools.eq_(np.sum(test_set[0]), 4361307.0)
    nose.tools.eq_(np.sum(test_set[2]), 32728516)


def test_DataPreprocessing():
    """Test the limit case of the class DataPreprocessing when all the parameters are given as input"""

    db_path = "./house-prices/house-prices.csv"

    # Nominal parameters:
    nominal = ["MS SubClass", "MS Zoning", "Street", "Alley", "Land Contour", "Lot Config", "Neighborhood",
               "Condition 1", "Condition 2", "Bldg Type", "House Style", "Roof Style", "Roof Matl", "Exterior 1st",
               "Exterior 2nd", "Mas Vnr Type", "Foundation", "Heating", "Central Air", "Garage Type", "Misc Feature",
               "Sale Type", "Sale Condition"]

    # Continuous parameters:
    continuous = ["Lot Frontage", "Lot Area", "Mas Vnr Area", "BsmtFin SF 1", "BsmtFin SF 2", "Bsmt Unf SF",
                  "Total Bsmt SF", "1st Flr SF", "2nd Flr SF", "Low Qual Fin SF", "Gr Liv Area", "Garage Area",
                  "Wood Deck SF", "Open Porch SF", "Enclosed Porch", "3Ssn Porch", "Screen Porch", "Pool Area",
                  "Misc Val"]

    # Ordinal parameters:
    ordinal = ["Lot Shape", "Utilities", "Land Slope", "Overall Qual", "Overall Cond", "Exter Qual", "Exter Cond",
               "Bsmt Qual", "Bsmt Cond", "Bsmt Exposure", "BsmtFin Type 1", "BsmtFin Type 2", "Heating QC",
               "Electrical",
               "Kitchen Qual", "Functional", "Fireplace Qu", "Garage Finish", "Garage Qual", "Garage Cond",
               "Paved Drive", "Pool QC", "Fence"]

    # Discrete parameters:
    discrete = ["Year Built", "Year Remod/Add", "Bsmt Full Bath", "Bsmt Half Bath", "Full Bath", "Half Bath",
                "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd", "Fireplaces", "Garage Yr Blt", "Garage Cars",
                "Mo Sold", "Yr Sold"]

    protocol = [0.8, 0.1, 0.1]

    house_price_db = HousePricesDatabase(db_path, continuous, discrete, ordinal,
                                         nominal, protocol)
    train_set, cv_set, test_set = house_price_db()

    preprocessing = DataPreprocessing(train_set, cv_set, test_set)
    X, y, mean_sale_price, std_sale_price = preprocessing()

    # Check correct number of samples in each set
    nose.tools.eq_(X[0].shape[0], 1492)
    nose.tools.eq_(X[1].shape[0], 186)
    nose.tools.eq_(X[2].shape[0], 187)
    # Check the correct number of parameters per sample
    nose.tools.eq_(X[0].shape[1], 333)
    nose.tools.eq_(X[1].shape[1], 333)
    nose.tools.eq_(X[2].shape[1], 333)

    # Check correct number of samples in each target set
    nose.tools.eq_(y[0].shape[0], 1492)
    nose.tools.eq_(y[1].shape[0], 186)
    nose.tools.eq_(y[2].shape[0], 187)

    # Verify that the same samples were used.
    np.testing.assert_array_almost_equal(np.sum(X[0]), 68632.00000, decimal=5)
    np.testing.assert_array_almost_equal(np.sum(X[1]), 8477.02924, decimal=5)
    np.testing.assert_array_almost_equal(np.sum(X[2]), 8372.82617, decimal=5)

    np.testing.assert_array_almost_equal(np.sum(y[0]), 1.421085e-13, decimal=18)
    np.testing.assert_array_almost_equal(np.sum(y[1]), -14.8419728, decimal=7)
    np.testing.assert_array_almost_equal(np.sum(y[2]), -23.7408063, decimal=7)

    # Check that z-normalization of target was done with correct mean and std
    np.testing.assert_array_almost_equal(mean_sale_price, 185637.85120, decimal=5)
    np.testing.assert_array_almost_equal(std_sale_price, 83643.41726, decimal=5)





