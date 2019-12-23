# AI in Trading NanoDegree (AITND)
This repository contains code for Udacity's [AI in Trading NanoDegree](https://www.udacity.com/course/nd880).

# Quantitative Trading

**Quant**
    - Those who build computational models of the world, that could be about financial markets
    - Apply scientific methods to finance
    - Uses math, statistics and technology to solve business problems (quantitative skills)
    - Work in hedge funds, commercial banks, asset management firms, data vendor firms etc.
    - Across different functions:
        - Research - to capture predictive signals in data to apply downstream to portfolios
        - Risk management
        - Portfolio construction
        - Data vending (preparing unstructured data to sell to financial industry)
        - Sales

### Stock prices

Shares of stock represent fractional ownership in a company, usually a company splits their stock into millions or billions of shares.

Two types of Stock:
- **Common** - shareholders receive a portion of profit as dividends, are able to vote on decisions and receive a portion of the remaining assets in case of liquidation
- **Preferred** - shareholders are promised a fixed amount of income each year, get paid before common stock holders get paid their dividends and usually do not have voting rights

**Capital gain** is the increase in the value of a stock

**Options: calls, puts, American, European**
Options give the owner the right to buy or sell at the strike price (a fixed price that is determined when the option is created), on or before an expiration date. The most common are call options and put options. Call options give the right to buy at the strike price; put options give the owner the right to sell at a fixed price. Some options allow the holder to “exercise” (buy or sell) at the strike price any time up to the expiration date. These are called “American options” by convention, even though this doesn’t mean that the options are traded in the Americas. Another class of options only allows the holder to exercise the option at the expiration date, but not earlier. These are called “European options” by convention, but again, European options don’t necessarily have to be traded in Europe.

**Forwards and Futures**
Futures and forwards contracts are similar, in that a buyer and seller both agree to make a future transaction at a predetermined price. Futures are standardized contracts that can be traded on a futures exchange, so this may be what people think of when discussing “forwards and futures”. Forward contracts are usually privately determined contracts between two parties. So an investor can trade futures contracts, but forward contracts are not designed to be traded like futures.

**Public versus private equity**
Public equity refers to stocks that can be traded on a stock exchange. Private equity refers to ownership in private companies, so the owners of private equity do not trade their shares on a stock exchange. Our course is primarily focused on public equity, which we’ll refer to as stocks, since the ability to buy and sell freely enables us to adjust our investments based on new or time-sensitive information.

**Security** is a financial instrument that has some type of monetary value such as stocks, bonds and options. Can be classified in three types:
    - **Debt**: represent money owed that needs to be paid such as government or corporate bonds or certificates of deposit, promise a fixed stream of income over time in the form of interest
    - **Derivative** - values depend on the prices of other assets such as options and futures contracts. For example an option gives the purchaser the right to but not the obligation to buy or sell the underlying asset at a specific price and date. The futures contract obligates the purchaser to buy or sell.
    - **Equity** - value of an owned asset minus the amount of all debts and liabilities on that asset or `net value`, stocks are equity securities since they represent ownership in a firm, private equity is a security representing interest in a private company

**Brokerage** acts as the middleman between buyers and sellers that will charge fees for transactions.

**Market Bubble** occurs when market participants drive stock prices above their value in relation to some system of valuation.

### Terminology Recap

Stock: An asset that represents ownership in a company. A claim on part of a corporation's assets and earnings. There are two main types, common and preferred.

Share: A single share represents partial ownership of a company relative to the total number of shares in existence.

Common Stock: One main type of stock; entitles the owner to receive dividends and to vote at shareholder meetings.

Preferred Stock: The other main type of stock; generally does not entail voting rights, but entitles the owner to a higher claim on the assets and earnings of a company.

Dividend: A partial distribution of a company's profits to shareholders.

Capital Gains: Profits that result from the sale of an asset at a price higher than the purchase price.

Security: A tradable financial asset.

Debt Security: Money that is owed and must be repaid, like government or corporate bonds, or certificates of deposit. Also called fixed-income securities.

Derivative Security: A financial instrument whereby its value is derived from other assets.

Equity: The value of an owned asset minus the amount of all debts on that asset.

Equity Security: A security that represents fractional ownership in an entity, such as stock.

Option Contract: A contract which gives the buyer the right, but not the obligation, to buy or sell an underlying asset at a specified price on or by a specified date

Futures Contract: A contract that obligates the buyer to buy or the seller to sell an asset at a predetermined price at a specified time in the future

Practice: `stock_data.ipynb`

### Market Mechanics

How to define price? Maximum price a buyer is willing to buy at and minimum price the seller is willing to sell at.

Stock price:

- as soon as it starts trading publicly, price is set given company metrics (revenue, profits, assets)
- after it is driven by **demand**
- how many people want to buy and how much they are willing to par or how many orders are placed and at what price
- markets keep electronic records of it all, limit orders (buy for a max of and sell for a min of), orders are matched according to these limits
- example: I submit a bid for 2 shares of NFLX at \$ 180, someone else submits a sell order of 4 NFLX shares at \$ 179.90, so there is match since the asking price is lower than the buying price. It's like an auction! Stock exchange is the authority.
- the stock exchange keeps track of the last price a specific stock was traded at (current price), someone can then sell at that price immediately (_market order_), the _market maker_ (brokerage) on the other end offers to buy at the same time potentially making profit from trading fees and commissions. The difference between the bid and ask price is known as the `bid-ask spread`
- the market maker brings **liquidity**: the property of a financial asset to be bought or sold without causing sharp changes in its price, also varies according to the market trading it (although differences are usually small). **Arbitrage** is buying and selling in different market to explore market inefficiency (difference in prices). Cash is considered the most liquid asset, because it can be readily traded for other assets.
- Stock exchange publishes **tick data** (data for each individual trade), intuitive to gauge health of a stock
- Important pieces of data: regularize time intervals and summarize data for each interval
    - ex: in 1 minute we capture: `open` `high` `low` `close` or OHLC
- Volume is also tracked - number of stocks traded during a specific time interval and large volumes of net buy orders tend to increase the stock price and large volumes of net sell orders tend to decrease stock price, hedge funds will spread their transactions across days because they alone influence the market by the large volume of their own transactions. Intra-day volume is important
- gaps in market data: 9:30am - 4:00pm operations, in order to also keep an eye for automated trading
- some exchanges allow premarket (4am to 9:30am) and postmarket (4pm to 8pm) trading, volume is typically low
- Note: Pre-market sessions (for the US market) are a period of time where stocks are very thinly traded. Market participants often use this to gauge the strength and direction of the market. Post-market sessions are often used by traders who want to trade on corporate announcements made after market closes, or for brokers to make whole of an incomplete client order.
- Beware of different market timezones.


![Market Mechanics](./images/market_mechanics.png)
![OHLC Chart](./images/OHLC.png)

Practice: `resample_data.ipynb`

### Data Processing

- Time resampling due to otherwise impossible to handle amount of tick data

![Market data](./images/market_data.png)

- Corporate actions: **stock splits** and **dividends**

- **market capitalization** is the dollar value of a company's outstanding shares

$$market \ cap=stock \ price * n_{shares \ outstanding}$$

- you may want to split a share to make it more liquid, more granularity. The stock price then drops and we need to normalize the data appropriately (for instance by doubling the price after a 2:1 split or better yet by halving the price before the 2:1 split so the newest adjusted price matches the market price). Historical datasets provide this _adjusted data_.

Aside: Although a stock split shouldn’t theoretically affect the market cap of a stock, in reality it does! There are some intriguing behavioral patterns that researchers have observed among traders. One seems to suggest that after a stock splits, and the price drops considerably, people seem to think it is going to go back up to the previous price (double or triple)! This creates an artificial demand for the stock, which in turn actually pushes up the price.


- cash **dividends**: partial cash distribution of company earnings. there is a cutoff date by which you have to buy the share to get future dividends on it (`ex-dividend date`). The price is also adjusted based on dividends. We normalize data prior to the ex-dividend date by dividing data by the adjusted price factor where D is the dividend and S is the stock price at ex-dividend date

$$adjusted \ price \ factor = 1+D/S$$

Now we have normalized historical market price data and want to get signals or indicators to trading strategies. What is the expected price of a stock?

One signal might come from the **simple moving average (rolling mean)** of the stock price data. So we can devise a trading strategy that looks at large deviations of these rolling means to generate trading signals. The threshold could be the standard deviation of the rolling window. Usually twice the std is used.

![Market data](./images/rolling_mean.png)
![Market data](./images/rolling_mean_2.png)

Note: Moving-window or “rolling” statistics are typically calculated with respect to a past period. Therefore, you won’t have a valid value at the beginning of the resulting time series, till you have one complete period. For instance, when you compute the Simple Moving Average with a 1-month or 30-day window, the result is undefined for the first 29 days. This is okay, and smart data analysis libraries like Pandas will mark these with a special “NA” or “nan” value (not zero, because that would be indiscernible from an actual zero value!). Subsequent processing or plotting will interpret those as missing data points.

- Missing days (weekends and holidays) might be worth treating.
    - The NYSE and NASDAQ average about 252 trading days a year. This is from 365.25(days on average per year) * 5/7(proportion work days per week) = 260.89 - 9(holidays) = 251.89 ~ 252.

- Survivor bias
    - Experiment A: Randomly select a smattering of 100 stocks that are trading today, simulate buying them in 2005, or whenever they went public, investing equally in each, and hold on to them till the present day. Don’t try to apply any strategy, just pick stocks randomly!
    - Experiment B: Randomly select another collection of 100 stocks, but this time, from those that were trading in 2005. Again, simulate buying them in 2005, investing uniformly, and hold on to them.
    - The average return from Experiment A would indeed be higher than that from B. this is important when analyzing efficiency of trading strategies using backtesting.

**Fundamental Analysis**
Fundamental analysis of a company involves looking at a company’s balance sheet and cash flow statements, which are usually updated every quarter, which is every three months when the company reports earnings. It’s important to keep in mind that looking at a single quarter’s metrics is only a snapshot of the company, and there are several metrics that each try to capture the health of the company, but in slightly different ways.

In a way, analyzing a company’s fundamentals is like going on a safari taking photographs of an antelope. A single still photo from one angle may tell you some things about the antelope, but taking multiple photos from different angles will give you a better view. Also, taking multiple photos over time will give you a sense of where the antelope is going. So before we introduce some commonly used metrics, please keep in mind that to get a better picture of a company that you’re trying to analyze, you’ll want to look at a collection of different measures over time.

**Sales Per Share**
A company’s revenue is based on its sales over that quarter, so we can think of sales and revenue as referring to the same thing. It’s a quick way to get a sense for how a company is doing, because we don’t have to subtract out cost of sales, which depends a bit on some accounting decisions. For example, if a company sells a million smartphones for a hundred dollars each over the past 3 months, then its revenue is $100 times 1 million, or \$100 million. If the company issued ten million shares, then its sales per share is \$100 million divided by ten million, or $10 per share.

You may be wondering why we bother dividing sales by the number of shares. This helps shareholders get a sense of how much the sales figures might impact a change in a single share price. You can imagine that if the company only issued 10 shares, a report of higher sales than forecasted would impact each share more than if the company issued ten million shares.

Also, note that sales of $10 per share probably does not mean that the shareholders will get $10 for each share that they own, or that their stock price will increase by \$10. It costs money for the company to make each smartphone. Let’s take a look at a metric that accounts for cost of sales next.

**Earnings Per Share
Earnings is the company’s revenue minus its cost of sales. Cost of sales refers to the cost of manufacturing the phone, employee wages, rent payments for office space, and the cost of equipment, like machines that make the phones. Earnings gives investors a sense of how much the equity of the company has changed over the past 3 months. Recall that stock represents a fractional ownership of a company’s equity.

Continuing with the smartphone company example, let’s say we can estimate the cost of sales per phone to be \$80 per phone. If the sales per phone is \$100, then the earnings per phone is \$100 - \$80 equals \$20 per phone. With sales of one million phones, earnings would be \$20 times one million, or \$20 million.

With ten million shares, this is earnings of \$20 million divided by ten million shares, which is \$2 earnings per share.

Note again, that this \$2 per share doesn’t mean that investors automatically receive an additional \$2 per share in their pocket. Let’s look at one way that investors do receive some of those earnings by looking at dividends.

Dividends Per Share
After a company has positive earnings, they may decide to either reinvest the cash in growing the company’s business. A company’s executives are usually expected to make spending decisions based on maximizing shareholder value. Whether this always happens in practice is debatable, but ideally, if the executives decide that re-investing in the business yields lower returns than an investor could gain from investing in a similar business at the same level of risk, they will give some of the earnings to shareholders as cash. This cash is referred to as dividends.

Let’s say, for example, that the smartphone company decides to return $10 million of its earnings to its shareholders. The dividend per share is then \$10 million divided by 10 million, or \$1 per share.

**Price to Earnings Ratio**
A term you’ll see often is price to earnings ratio, or PE ratio for short. This is the stock’s current market price divided by its most recently reported earnings per share (EPS). You can sort of interpret the PE ratio as how much the company is valued compared to how much money it made. It’s important to be careful about how we interpret a high or low PE ratio, because we can’t say whether a PE ratio is good or bad by looking at it in isolation. Let’s first look at where the price comes from. This market price of a share is based on the collective estimates by investors of the company’s current equity plus its future earnings. The future earnings are based on estimates of future cash flow, which are then adjusted to their present-day value, or Present Value (PV). This is getting a bit outside the scope of what you’ll need to know for this course, but the point we want you to remember is that the market price of a stock is based on both its current assets minus liabilities, but also estimates of the company’s future performance.

Now coming back to the PE ratio. What does it mean to have a high PE ratio? A company may have low or negative earnings, but a high stock price. Why do you think that is? You may have heard of certain startups that are valued at billions of dollars, and yet have low earnings. This is because investors expect potential for high earnings growth, based on the trajectory of past earnings growth. This also means that investors are estimating that the high stock price relative to earnings will be justified by high future earnings. On the other hand, it’s also possible that investor optimism towards the company’s future never materializes, in which case the stock may be overpriced.

Note also that a low PE ratio can also be due to different underlying reasons. An example of a company with a low PE ratio may be one that has high and stable earnings, but less expectations for future growth. Since the company may decide that its investors are better off receiving earnings as dividends instead of reinvesting earnings into the business, the earnings will be distributed as cash to shareholders. This also means that the stock price itself represents the value of the company excluding the cash that was already distributed to these shareholders. Again, keep in mind that a low PE ratio can also be a sign of something else. If a company is expected to face pressure from competitors or government regulation that reduce their expectations for future earnings, then investors may pay a lower price for each share, and that could also result in a lower PE ratio.

In practice, you’ll want to see how a company’s PE ratio compares to other similar companies in the same industry and same geographic region.

You’ll see PE ratios again in later lessons, so for now, just remember that it’s one of many ways to take a snapshot of a company’s financial health.

- We want strategies that yield good returns with reduced risk.

- Mutual funds takes money from multiple investors and intermediate the trading for them. They can track performance on specific sectors such as tech, infrastructure, communications etc.

- Exchange traded funds (ETFs) are ones where you buy the shares in the market, they usually have good growth as long as the sector or index they are tracking perform well. They mitigate risk and you don't to pay a broker to invest in each company individually. A popular one is `S&P 500` (500 companies with large market cap in the NYEX or NASDAQ). Their composition change over time. ETF compositional data is another interesting source of information for trading strategies.

### Stock Returns

Percentage return: $r=(p_{t}-p_{t-1})/p_{t-1}$
Log return: $R=ln(p_{t}/p_{t-1})=ln(r+1)$
If r is close to 0, the log return is close to the percentage return.

Rates of Compounding
A statement by a bank that the interest rate on one-year deposits is 4% per year sounds straightforward and unambiguous. In fact, its precise meaning depends on the way the interest rate is measured. For an interest rate statement to be clear, the magnitude and time dependence of the rate of interest, as well as the frequency of compounding, must be clearly stated.

$$p_t=p_{t-1}(1+r/n)^n$$

With more frequent compounding, the value at 1 year increases but then seems to level off. If you assumed that the benefit of compounding more and more frequently had a limit, you would be right! How do we calculate this limit?

$$lim_{n\rightarrow \infty}=e^r$$

Compounding infinitely often is called continuous compounding.

The **continuously compounded annual return** equals $\ln(p_t/p_{t-1})$. But what is this quantity? It’s just the log return! This is why you might hear log returns called continuously compounded returns. The continuously compounded rate of return is additive over time.

Multiplication of many small numbers can result in the problem that the product is smaller than the smallest number representable in computer memory. Sometimes the computation will incorrectly yield the value 0. This is called arithmetic underflow. The use of logarithms can help with this, since it enables the representation of much smaller (and much larger) numbers.

**Returns and the Historical Record**

Let's look at the adjusted closing price of Apple stock (AAPL) from 1980 up until the present.

![Market data](./images/log_returns_1.png)

These plot look almost the same—that's because the returns and log returns for these daily data have very similar values. This is because daily returns are small—the values are close to 0, so the property $\ln(1 + r) \approx r$ applies. But we're interested in the distribution of these values, so let's look at a histogram.

![Market data](./images/log_returns_2.png)

Here we've plotted a histogram of AAPL's log returns from 1980 to the present, and we've overlaid a scaled normal distribution. We can see a few things right away from this plot. First, the values are centered around 0, and in fact look roughly normal. However, the tails of the histogram clearly lie above the tails of the normal distribution. We call these "fat tails".

In general, the normal distribution can be a reasonable approximation for short-term returns and log returns for some applications. However, many analyses have shown that the data do not conform perfectly to a normal distribution, and often deviate significantly in the tails. The significance of this is that the normal distribution predicts fewer extreme events than are actually observed. The conversation about the best model for the distribution of returns has been going on for at least the past century. The best model will depend on exactly what your analysis seeks to achieve.

Practice: `calculate_returns.ipynb`

Normality and Long-Term Investments

Based on historical data, it may be reasonable to consider short-term returns as approximately normally distributed for some purposes. However, even if short-term returns are normally distributed, long-term returns cannot be. If $r_1 = \frac{p_1 - p_0}{p_0}$ and $r_2 = \frac{p_2 - p_1}{p_1}$ are normally distributed, the sum of these, $r_1 + r_2$ would be normally distributed. But the two-period return is not the sum of the one-period returns. The two-period return equals $(1+r_1)(1+r_2)$ which is not normal and becomes noticeably less normal as the product grows over time.

So long-term prices and cumulative returns can be modeled as approximately lognormally distributed because they are products of independently, identically distributed (IID) random variables. On the other hand, log returns sum over time. Therefore, if $R_1 = \ln\left(\frac{p_1}{p_0}\right)$ and $R_2 = \ln\left(\frac{p_2}{p_1}\right)$ are normal, their sum, the two-period log return, is also normal. Even if they are not normal, as long as they are IID, their long-term sum will be approximately normal, thanks to the Central Limit Theorem. This is one reason why using log returns can be convenient for modeling purposes.

![Log-normal distribution of stock prices](./images/log_normal_dist.png)

So these are some generally accepted reasons that quantitative analysts use log returns:

1. Log returns can be interpreted as continuously compounded returns.
2. Log returns are time-additive. The multi-period log return is simply the sum of single period log returns.
3. The use of log returns prevents security prices from becoming negative in models of security returns.
4. For many purposes, log returns of a security can be reasonably modeled as distributed according to a normal distribution.
5. When returns and log returns are small (their absolute values are much less than 1), their values are approximately equal.
6. Logarithms can help make an algorithm more numerically stable.

### Momentum Trading

**Trading strategy** is a set of rules to determine what stocks to trade, when to trade, and how much money to invest.

**Momentum** is an empirically observed phenomenon that past "winners" tend to continue to outperform other stocks and past "losers" continue to underperform. So it might be a good idea to buy over-performers and sell under-performers, capitalizing in the continuation of their movement.

Portfolio
A portfolio is a collection of investments held and/or managed by an investment company, hedge fund, financial institution or individual.

**Long**
A long (or long position) is the purchase of an asset under the expectation that the price of the asset will rise.

**Short**
A short (or short position) is the selling of an asset under the expectation that the price of the asset will decline. In practice, an investor profits from a short position by borrowing shares from a brokerage firm (agreeing to pay an interest rate as a fee), selling them on the open market, and later buying them back on the open market at a lower price and returning them to the brokerage firm.

![Short position](./images/short.png)

Momentum-based trading strategy:

![](./images/momentum_trading.png)

Let's say we have a timeseries of monthly returns and the mean return is 0.53%. How do we know if the trading strategy actually yielded returns that on average are positive or could this positive mean be due random fluctuations?
We can use the t-test to test whether the mean of our sample differs in a statistically significant way from the theoretical expectation.
$$t=\bar x / SE_{\bar x} \ where\ SE_{\bar x}=std/\sqrt n$$

We measure the probability of getting the actual mean if the true mean is zero or the p value. If the p value is small we infer that is unlikely that the true mean is zero. We set a threshold to label our inferences $\alpha%. If $\alpha=0.1$ we are saying that we are ok in rejecting the null hypothesis when the true mean is 0 in 10% of hypothetical uses of this test.

![](./images/t_stats.png)

In finance, alpha refers to multiple distinct but somewhat related ideas. The common thread among these definitions is that alpha is the extra value that an investment professional can add to the performance of an investment.

One specific definition of alpha is the extra return that an actively managed fund can deliver, that exceeds the performance of passively investing (buy and hold) in a portfolio of stocks. Another specific definition of alpha, which we’ll primarily focus on in this course, is that of an alpha vector.

An alpha vector is a list of numbers, one for each stock in a portfolio, that gives us a signal as to the relative future performance of these stocks.

**Test Returns for Statistical Significance**

Remember that if the sample mean is $\bar{x}$, and the sample standard deviation, s, equals:

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^n{(x_i-\bar{x})}^2}$$

then the standard error, $s_{\bar{x}}$, equals:

$$s_{\bar{x}} = \frac{s}{\sqrt{n}}$$

where n is the number of observations in the sample. Then in the case that we are testing the hypothesis that the population mean, μ, equals 0, the t-statistic, t, equals:

$$t = \frac{\bar{x}-\mu}{s_{\bar{x}}} = \frac{\bar{x}-0}{s_{\bar{x}}} = \frac{\bar{x}}{s_{\bar{x}}}$$

​Note: we use `scipy.stats` as the package to perform statistical analysis here.

```
import pandas as pd
import numpy as np
import scipy.stats as stats

def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # TODO: Perform one-tailed t-test on net_returns
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divde the p-value by 2 to get the results of a one-tailed p-value.
    null_hypothesis = 0.0
    t, p = stats.ttest_1samp(net_returns, null_hypothesis)

    return t, p/2
```
Low p-values tell us that if the true mean is 0, we would be unlikely to observe a mean as or more "extreme" than the mean we observed.

Practice: `dtype.ipynb` and `top_and_bottom_performing.ipynb`

### Quant Workflow

It all starts with a specific hypothesis. For instance _stocks that are discussed in the news are likely to go up_ is too vague and ergo does not lead to testable predictions. A improved hypothesis would be _stocks whose name or ticker appears on the landing page of the Wall Street Journal website will increase in price by 1% one day following its appearance_.

Market research is key:
    - news
    - blogs
    - books
    - study known strategies
    - academic papers
    - meetups and conferences

![](./images/workflow.png)

Several types of trading strategies:

1. Single asset like S&P500 index
2. Pairwise - compares relative movements of related tickers (same sector for instance)
3. Cross-sectional or equity statistical arbitrage or equity market neutral investing - compares several stocks to determine which to hold in long and short portfolios to benefit from transient phenomena

![](./images/equity_neutral.png)

4. Alternative-data driven (satellite imagery, social media, geolocation, consumer transaction data etc)

Large hedge funds usually apply 3. and 4. given the capacity to invest lots of capital and different ideas to uncover signals (use hard to find and difficult to work with data).

![](./images/strategy_layout.png)

![](./images/alpha.png)

A trading signal is a general term for any numerical signal that informs a trade. In practice, several alphas or signals are combined in a strategy - the idea of **model stacking / ensembling**.

In finance risk refers to uncertainty or variability on returns.
1. systematic risk - inherent to entire market (inflation, recession, interest rates, GDP)
    - sector specific risk - inherent to sectors (regulation, legislation, material costs)
2. idiosyncratic risk - inherent to specific stocks (labor strike, managerial changes)
