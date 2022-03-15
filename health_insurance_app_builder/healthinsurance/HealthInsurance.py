import pickle
import pandas as pd

class HealthInsurance( object ):
    def __init__ (self):
        self.age_scaler            = pickle.load( open( 'encoders/age_scaler.pkl', 'rb' ) )
        self.annual_scaler         = pickle.load( open( 'encoders/annual_scaler.pkl', 'rb' ) )
        self.gender_encoding       = pickle.load( open( 'encoders/gender_encoding.pkl', 'rb' ) )
        self.policy_sales_encoding = pickle.load( open( 'encoders/policy_sales_encoding.pkl', 'rb' ) )
        self.region_code_encoding  = pickle.load( open( 'encoders/region_code_encoding.pkl', 'rb' ) )
        self.vintage_scaler        = pickle.load( open( 'encoders/vintage_scaler.pkl', 'rb' ) )
        
    def feature_engineering( self, df2 ):

        # lowercase columns
        df2.columns = [x.lower() for x in df2.columns]

        # vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply( lambda x: 'below_1_year' if x == '< 1 Year' else 
                                                                 'between_1_2_years' if x == '1-2 Year' else 'over_2_years' )

        # vehicle damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 )
        
        return df2
        
    def data_preparation( self, df5 ):

        ## 5.1. Normalization

        # annual premium - normal curve
        
        df5['annual_premium'] = self.annual_scaler.transform( df5[['annual_premium']].values )
        
        ## 5.2. Rescaling

        # age
        df5['age'] = self.age_scaler.transform( df5[['age']].values )
        
        # vintage
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )
    
        ## 5.3. Encoding

        # region code - Target Encoding

        df5['region_code'] = df5['region_code'].map( self.region_code_encoding )
    
        # policy sales channel - Frequency Encoding

        df5['policy_sales_channel'] = df5['policy_sales_channel'].map( self.policy_sales_encoding )
       
        # gender

        df5['gender'] = self.gender_encoding.transform( df5['gender'] )

        # vehicle age - One Hot Encoding
        df5 = pd.get_dummies( df5, prefix='vehicle_age', columns=['vehicle_age'] )
        
        # COLS SELECTED
        selected_cols = [ 'vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage',
                          'policy_sales_channel', 'previously_insured' ]
        
        return df5[ selected_cols ]
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into original data
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )
