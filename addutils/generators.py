# The MIT License (MIT)
# 
# Copyright (c) 2015 addfor s.r.l.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

import pandas as pd
import numpy as np

try:
    from pandas_datareader.data import DataReader
except ImportError:
    pass

WORK_DIRECTORY = 'work'
DATA_DIRECTORY = 'example_data'


def work_directory_path(location, file_name):
    return os.path.join(location, WORK_DIRECTORY, file_name)


def get_data_name(location, name):
    return os.path.join(location, DATA_DIRECTORY, name)


def p01_d2csv(location):
    d = dict(a=pd.Series(['one', 'one', 'two', 'three', 'two']),
             b=pd.Series(['x', 'y', 'y', 'x', 'y']),
             c=pd.Series(np.random.randn(5)))
    d2 = pd.DataFrame(d)
    d2.to_csv(work_directory_path(location, 'p01_d2.csv'))
    return d2


def p01_d3csv(location):
    comuni = pd.read_csv(get_data_name(location, 'tabella_comuni_italiani.txt'),
                         sep=';', header=0)
    comuni.to_csv(work_directory_path(location, 'p01_d3.csv'), index=False)
    return comuni


def p01_d4csv(location):
    idx = [('Fra', 'one', 'x'),
           ('Fra', 'two', 'y'),
           ('Fra', 'two', 'z'),
           ('Ger', 'one', 'x'),
           ('Jap', 'one', 'x'),
           ('Jap', 'two', 'x'),
           ('USA', 'one', 'y'),
           ('USA', 'one', 'z')]
    index = pd.MultiIndex.from_tuples(idx, names=['Country', 'Number', 'Dir'])
    d4 = pd.DataFrame(np.random.randn(8, 3), index=index)
    d4.to_csv(work_directory_path(location, 'p01_d4.csv'))
    return d4


def p01_prices(location):
    symbols = ['AAPL', 'JNJ', 'XOM', 'GOOG']
    data = dict([(sym, DataReader(sym, 'yahoo')['Close']) for sym in symbols])
    df = pd.DataFrame.from_dict(data)
    df.ix[-7:-1].to_csv(work_directory_path(location, 'p01_prices.txt'))


def p01_volumes(location):
    symbols = ['AAPL', 'JNJ', 'XOM']
    data = dict([(sym, DataReader(sym, 'yahoo')['Volume']) for sym in symbols])
    df = pd.DataFrame.from_dict(data)
    df.ix[-7:-3].to_csv(work_directory_path(location, 'p01_volumes.txt'))
    return df.ix[-7:-3]


def p03_DAX(location):
    dax = DataReader('^GDAXI', 'yahoo', start='01/01/2000')
    dax.to_csv(work_directory_path(location, 'p03_DAX.csv'))
    return dax


def p03_AAPL(location):
    dax = DataReader('AAPL', 'yahoo', start='01/01/2000')
    dax.to_csv(work_directory_path(location, 'p03_AAPL.csv'))
    return dax


def p06_d3csv(location):
    d2 = pd.DataFrame(
        {'City': ['New York', ' frisco', 'houston', ' taft', 'venice'],
         'State': [' NY ', 'CA', '  tx ', '   OK', '  IL'],
         'Name': ['Roy', 'Johnn', 'Jim', 'Paul', 'Ross'],
         'Revenues': ['1250', '840', '349', '1100', '900']})
    d2.to_csv(work_directory_path(location, 'p06_d2.txt'))
    return d2


def p06_d2csv(location):
    d3 = pd.DataFrame({'Quantity': ['1-one', '1-one', '2-two', '3-three'] * 6,
                       'Axis': ['X', 'Y', 'Z'] * 8,
                       'Type': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                       'N1': np.random.randn(24),
                       'N2': np.random.randn(24)})
    d3.to_csv(work_directory_path(location, 'p06_d3.txt'))
    return d3


def p07_d1csv(location):
    d1 = pd.DataFrame(
        {'State': ['NE', 'KY', 'CO', 'CO', 'KY', 'KY', 'CO', 'NE', 'CO'],
         'City': ['Page', 'Stone', 'Rye', 'Rye', 'Dema', 'Keavy', 'Rye',
                  'Cairo', 'Dumont'],
         'Views': [10, 9, 3, 7, 4, 2, 1, 8, 12],
         'Likes': [4, 3, 0, 2, 1, 1, 0, 3, 7]})
    d1.to_csv(work_directory_path(location, 'p07_d1.txt'))
    return d1


def p07_d2csv(location):
    import random;

    random.seed(0)
    import string

    N = 1000

    def rands(n):
        choices = string.ascii_uppercase
        return ''.join([random.choice(choices) for _ in xrange(n)])

    tickers = np.array([rands(5) for _ in xrange(N)])

    # Create a DataFrame containing 3 columns representing
    # hypothetical, but random portfolios for a subset of tickers:
    d2 = pd.DataFrame({'Momentum': np.random.randn(500) / 200 + 0.03,
                       'Value': np.random.randn(500) / 200 + 0.08,
                       'ShortInterest': np.random.randn(500) / 200 - 0.02},
                      index=tickers.take(np.random.permutation(N)[:500]))

    # Next, let's create a random industry classification for the tickers.
    ind_names = np.array(['FINANCIAL', 'TECH'])
    sampler = np.random.randint(0, len(ind_names), N)
    industries = pd.Series(ind_names.take(sampler), index=tickers,
                           name='industry')
    d2['Industry'] = industries

    d2.to_csv(work_directory_path(location, 'p07_d2.csv'))
    return d2


def p07_portfolioh5(location):
    import random;

    random.seed(0)
    import string

    N = 1000

    def rands(n):
        choices = string.ascii_uppercase
        return ''.join([random.choice(choices) for _ in xrange(n)])

    tickers = np.array([rands(5) for _ in xrange(N)])
    fac1, fac2, fac3 = np.random.rand(3, 1000)
    ticker_subset = tickers.take(np.random.permutation(N)[:1000])

    # portfolio = weighted sum of factors plus noise
    portfolio = pd.Series(
        0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + np.random.rand(1000),
        index=ticker_subset)
    factors = pd.DataFrame({'f1': fac1, 'f2': fac2, 'f3': fac3},
                           index=ticker_subset)

    h5file = pd.HDFStore(work_directory_path(location, 'p07_portfolio.h5'))
    h5file['factors'] = factors
    h5file['portfolio'] = portfolio
    h5file.close()
    return None


def baby_names(location):
    import zipfile

    path = work_directory_path(location, 'babynames.zip')
    opath = work_directory_path(location, "")
    z = zipfile.ZipFile(path, "r")
    z.extractall(path=opath)
    return None


generators = {
    'baby_names/': baby_names,
    'p07_portfolio.h5': p07_portfolioh5,
    'p07_d2.csv': p07_d2csv,
    'p07_d1.txt': p07_d1csv,
    'p06_d3.txt': p06_d3csv,
    'p06_d2.txt': p06_d2csv,
    'p03_DAX.csv': p03_DAX,
    'p03_AAPL.csv': p03_AAPL,
    'p01_prices.txt': p01_prices,
    'p01_d2.csv': p01_d2csv,
    'p01_d3.csv': p01_d3csv,
    'p01_d4.csv': p01_d4csv,
    'p01_volumes.txt': p01_volumes,
}
