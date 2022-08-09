from pyspark.sql.types import *

gaia_source_schema = StructType([
            StructField('solution_id', LongType(), True),
            StructField('designation', StringType(), True),
            StructField('source_id', LongType(), True),
            StructField('random_index', LongType(), True),
            StructField('ref_epoch', FloatType(), True),
            StructField('ra', DoubleType(), True),
            StructField('ra_error', DoubleType(), True),
            StructField('dec', DoubleType(), True),
            StructField('dec_error', DoubleType(), True),
            StructField('parallax', DoubleType(), True),
            StructField('parallax_error', DoubleType(), True),
            StructField('parallax_over_error', FloatType(), True),
            StructField('pm', FloatType(), True),
            StructField('pmra', DoubleType(), True),
            StructField('pmra_error', FloatType(), True),
            StructField('pmdec', DoubleType(), True),
            StructField('pmdec_error', FloatType(), True),
            StructField('ra_dec_corr', FloatType(), True),
            StructField('ra_parallax_corr', FloatType(), True),
            StructField('ra_pmra_corr', FloatType(), True),
            StructField('ra_pmdec_corr', FloatType(), True),
            StructField('dec_parallax_corr', FloatType(), True),
            StructField('dec_pmra_corr', FloatType(), True),
            StructField('dec_pmdec_corr', FloatType(), True),
            StructField('parallax_pmra_corr', FloatType(), True),
            StructField('parallax_pmdec_corr', FloatType(), True),
            StructField('pmra_pmdec_corr', FloatType(), True),
            StructField('astrometric_n_obs_al', ShortType(), True),
            StructField('astrometric_n_obs_ac', ShortType(), True),
            StructField('astrometric_n_good_obs_al', ShortType(), True),
            StructField('astrometric_n_bad_obs_al', ShortType(), True),
            StructField('astrometric_gof_al', FloatType(), True),
            StructField('astrometric_chi2_al', FloatType(), True),
            StructField('astrometric_excess_noise', FloatType(), True),
            StructField('astrometric_excess_noise_sig', FloatType(), True),
            StructField('astrometric_params_solved', ShortType(), True),
            StructField('astrometric_primary_flag', BooleanType(), True),
            StructField('nu_eff_used_in_astrometry', FloatType(), True),
            StructField('pseudocolour', FloatType(), True),
            StructField('pseudocolour_error', FloatType(), True),
            StructField('ra_pseudocolour_corr', FloatType(), True),
            StructField('dec_pseudocolour_corr', FloatType(), True),
            StructField('parallax_pseudocolour_corr', FloatType(), True),
            StructField('pmra_pseudocolour_corr', FloatType(), True),
            StructField('pmdec_pseudocolour_corr', FloatType(), True),
            StructField('astrometric_matched_transits', ShortType(), True),
            StructField('visibility_periods_used', ShortType(), True),
            StructField('astrometric_sigma5d_max', FloatType(), True),
            StructField('matched_transits', ShortType(), True),
            StructField('new_matched_transits', ShortType(), True),
            StructField('matched_transits_removed', ShortType(), True),
            StructField('ipd_gof_harmonic_amplitude', FloatType(), True),
            StructField('ipd_gof_harmonic_phase', FloatType(), True),
            StructField('ipd_frac_multi_peak', ShortType(), True),
            StructField('ipd_frac_odd_win', ShortType(), True),
            StructField('ruwe', FloatType(), True),
            StructField('scan_direction_strength_k1', FloatType(), True),
            StructField('scan_direction_strength_k2', FloatType(), True),
            StructField('scan_direction_strength_k3', FloatType(), True),
            StructField('scan_direction_strength_k4', FloatType(), True),
            StructField('scan_direction_mean_k1', FloatType(), True),
            StructField('scan_direction_mean_k2', FloatType(), True),
            StructField('scan_direction_mean_k3', FloatType(), True),
            StructField('scan_direction_mean_k4', FloatType(), True),
            StructField('duplicated_source', BooleanType(), True),
            StructField('phot_g_n_obs', ShortType(), True),
            StructField('phot_g_mean_flux', DoubleType(), True),
            StructField('phot_g_mean_flux_error', FloatType(), True),
            StructField('phot_g_mean_flux_over_error', FloatType(), True),
            StructField('phot_g_mean_mag', FloatType(), True),
            StructField('phot_bp_n_obs', ShortType(), True),
            StructField('phot_bp_mean_flux', DoubleType(), True),
            StructField('phot_bp_mean_flux_error', FloatType(), True),
            StructField('phot_bp_mean_flux_over_error', FloatType(), True),
            StructField('phot_bp_mean_mag', FloatType(), True),
            StructField('phot_rp_n_obs', ShortType(), True),
            StructField('phot_rp_mean_flux', DoubleType(), True),
            StructField('phot_rp_mean_flux_error', FloatType(), True),
            StructField('phot_rp_mean_flux_over_error', FloatType(), True),
            StructField('phot_rp_mean_mag', FloatType(), True),
            StructField('phot_bp_n_contaminated_transits', ShortType(), True),
            StructField('phot_bp_n_blended_transits', ShortType(), True),
            StructField('phot_rp_n_contaminated_transits', ShortType(), True),
            StructField('phot_rp_n_blended_transits', ShortType(), True),
            StructField('phot_proc_mode', ShortType(), True),
            StructField('phot_bp_rp_excess_factor', FloatType(), True),
            StructField('bp_rp', FloatType(), True),
            StructField('bp_g', FloatType(), True),
            StructField('g_rp', FloatType(), True),
            StructField('dr2_radial_velocity', FloatType(), True),
            StructField('dr2_radial_velocity_error', FloatType(), True),
            StructField('dr2_rv_nb_transits', ShortType(), True),
            StructField('dr2_rv_template_teff', FloatType(), True),
            StructField('dr2_rv_template_logg', FloatType(), True),
            StructField('dr2_rv_template_fe_h', FloatType(), True),
            StructField('l', DoubleType(), True),
            StructField('b', DoubleType(), True),
            StructField('ecl_lon', DoubleType(), True),
            StructField('ecl_lat', DoubleType(), True),
])

twomass_psc_schema = StructType([
            StructField('ra', DoubleType(), True),
            StructField('dec', DoubleType(), True),
            StructField('err_maj', FloatType(), True),
            StructField('err_min', FloatType(), True),
            StructField('err_ang', ShortType(), True),
            StructField('designation', StringType(), True),
            StructField('j_m', FloatType(), True),
            StructField('j_cmsig', FloatType(), True),
            StructField('j_msigcom', FloatType(), True),
            StructField('j_snr', FloatType(), True),
            StructField('h_m', FloatType(), True),
            StructField('h_cmsig', FloatType(), True),
            StructField('h_msigcom', FloatType(), True),
            StructField('h_snr', FloatType(), True),
            StructField('k_m', FloatType(), True),
            StructField('k_cmsig', FloatType(), True),
            StructField('k_msigcom', FloatType(), True),
            StructField('k_snr', FloatType(), True),
            StructField('ph_qual', StringType(), True),
            StructField('rd_flg', StringType(), True),
            StructField('bl_flg', StringType(), True),
            StructField('cc_flg', StringType(), True),
            StructField('ndet', StringType(), True),
            StructField('prox', FloatType(), True),
            StructField('pxpa', ShortType(), True),
            StructField('pxcntr', IntegerType(), True),
            StructField('gal_contam', ShortType(), True),
            StructField('mp_flg', ShortType(), True),
            StructField('pts_key', IntegerType(), True),
            StructField('hemis', StringType(), True),
            StructField('date', DateType(), True),
            StructField('scan', ShortType(), True),
            StructField('glon', FloatType(), True),
            StructField('glat', FloatType(), True),
            StructField('x_scan', FloatType(), True),
            StructField('jdate', DoubleType(), True),
            StructField('j_psfchi', FloatType(), True),
            StructField('h_psfchi', FloatType(), True),
            StructField('k_psfchi', FloatType(), True),
            StructField('j_m_stdap', FloatType(), True),
            StructField('j_msig_stdap', FloatType(), True),
            StructField('h_m_stdap', FloatType(), True),
            StructField('h_msig_stdap', FloatType(), True),
            StructField('k_m_stdap', FloatType(), True),
            StructField('k_msig_stdap', FloatType(), True),
            StructField('dist_edge_ns', IntegerType(), True),
            StructField('dist_edge_ew', IntegerType(), True),
            StructField('dist_edge_flg', StringType(), True),
            StructField('dup_src', ShortType(), True),
            StructField('use_src', ShortType(), True),
            StructField('a', StringType(), True),
            StructField('dist_opt', FloatType(), True),
            StructField('phi_opt', ShortType(), True),
            StructField('b_m_opt', FloatType(), True),
            StructField('vr_m_opt', FloatType(), True),
            StructField('nopt_mchs', ShortType(), True),
            StructField('ext_key', IntegerType(), True),
            StructField('scan_key', IntegerType(), True),
            StructField('coadd_key', IntegerType(), True),
            StructField('coadd', ShortType(), True),
])

allwise_sc_schema = StructType([
            StructField('designation', StringType(), True),
            StructField('ra', DoubleType(), True),
            StructField('dec', DoubleType(), True),
            StructField('sigra', DoubleType(), True),
            StructField('sigdec', DoubleType(), True),
            StructField('sigradec', DoubleType(), True),
            StructField('glon', DoubleType(), True),
            StructField('glat', DoubleType(), True),
            StructField('elon', DoubleType(), True),
            StructField('elat', DoubleType(), True),
            StructField('wx', DoubleType(), True),
            StructField('wy', DoubleType(), True),
            StructField('cntr', LongType(), True),
            StructField('src_id', StringType(), True),
            StructField('coadd_id', StringType(), True),
            StructField('src', IntegerType(), True),
            StructField('w1mpro', DoubleType(), True),
            StructField('w1sigmpro', DoubleType(), True),
            StructField('w1snr', DoubleType(), True),
            StructField('w1rchi2', FloatType(), True),
            StructField('w2mpro', DoubleType(), True),
            StructField('w2sigmpro', DoubleType(), True),
            StructField('w2snr', DoubleType(), True),
            StructField('w2rchi2', FloatType(), True),
            StructField('w3mpro', DoubleType(), True),
            StructField('w3sigmpro', DoubleType(), True),
            StructField('w3snr', DoubleType(), True),
            StructField('w3rchi2', FloatType(), True),
            StructField('w4mpro', DoubleType(), True),
            StructField('w4sigmpro', DoubleType(), True),
            StructField('w4snr', DoubleType(), True),
            StructField('w4rchi2', FloatType(), True),
            StructField('rchi2', FloatType(), True),
            StructField('nb', IntegerType(), True),
            StructField('na', IntegerType(), True),
            StructField('w1sat', DoubleType(), True),
            StructField('w2sat', DoubleType(), True),
            StructField('w3sat', DoubleType(), True),
            StructField('w4sat', DoubleType(), True),
            StructField('satnum', StringType(), True),
            StructField('ra_pm', DoubleType(), True),
            StructField('dec_pm', DoubleType(), True),
            StructField('sigra_pm', DoubleType(), True),
            StructField('sigdec_pm', DoubleType(), True),
            StructField('sigradec_pm', DoubleType(), True),
            StructField('pmra', IntegerType(), True),
            StructField('sigpmra', IntegerType(), True),
            StructField('pmdec', IntegerType(), True),
            StructField('sigpmdec', IntegerType(), True),
            StructField('w1rchi2_pm', FloatType(), True),
            StructField('w2rchi2_pm', FloatType(), True),
            StructField('w3rchi2_pm', FloatType(), True),
            StructField('w4rchi2_pm', FloatType(), True),
            StructField('rchi2_pm', FloatType(), True),
            StructField('pmcode', StringType(), True),
            StructField('cc_flags', StringType(), True),
            StructField('rel', StringType(), True),
            StructField('ext_flg', IntegerType(), True),
            StructField('var_flg', StringType(), True),
            StructField('ph_qual', StringType(), True),
            StructField('det_bit', IntegerType(), True),
            StructField('moon_lev', StringType(), True),
            StructField('w1nm', IntegerType(), True),
            StructField('w1m', IntegerType(), True),
            StructField('w2nm', IntegerType(), True),
            StructField('w2m', IntegerType(), True),
            StructField('w3nm', IntegerType(), True),
            StructField('w3m', IntegerType(), True),
            StructField('w4nm', IntegerType(), True),
            StructField('w4m', IntegerType(), True),
            StructField('w1cov', DoubleType(), True),
            StructField('w2cov', DoubleType(), True),
            StructField('w3cov', DoubleType(), True),
            StructField('w4cov', DoubleType(), True),
            StructField('w1cc_map', IntegerType(), True),
            StructField('w1cc_map_str', StringType(), True),
            StructField('w2cc_map', IntegerType(), True),
            StructField('w2cc_map_str', StringType(), True),
            StructField('w3cc_map', IntegerType(), True),
            StructField('w3cc_map_str', StringType(), True),
            StructField('w4cc_map', IntegerType(), True),
            StructField('w4cc_map_str', StringType(), True),
            StructField('best_use_cntr', LongType(), True),
            StructField('ngrp', ShortType(), True),
            StructField('w1flux', FloatType(), True),
            StructField('w1sigflux', FloatType(), True),
            StructField('w1sky', DoubleType(), True),
            StructField('w1sigsk', DoubleType(), True),
            StructField('w1conf', DoubleType(), True),
            StructField('w2flux', FloatType(), True),
            StructField('w2sigflux', FloatType(), True),
            StructField('w2sky', DoubleType(), True),
            StructField('w2sigsk', DoubleType(), True),
            StructField('w2conf', DoubleType(), True),
            StructField('w3flux', FloatType(), True),
            StructField('w3sigflux', FloatType(), True),
            StructField('w3sky', DoubleType(), True),
            StructField('w3sigsk', DoubleType(), True),
            StructField('w3conf', DoubleType(), True),
            StructField('w4flux', FloatType(), True),
            StructField('w4sigflux', FloatType(), True),
            StructField('w4sky', DoubleType(), True),
            StructField('w4sigsk', DoubleType(), True),
            StructField('w4conf', DoubleType(), True),
            StructField('w1mag', DoubleType(), True),
            StructField('w1sigm', DoubleType(), True),
            StructField('w1flg', IntegerType(), True),
            StructField('w1mcor', DoubleType(), True),
            StructField('w2mag', DoubleType(), True),
            StructField('w2sigm', DoubleType(), True),
            StructField('w2flg', IntegerType(), True),
            StructField('w2mcor', DoubleType(), True),
            StructField('w3mag', DoubleType(), True),
            StructField('w3sigm', DoubleType(), True),
            StructField('w3flg', IntegerType(), True),
            StructField('w3mcor', DoubleType(), True),
            StructField('w4mag', DoubleType(), True),
            StructField('w4sigm', DoubleType(), True),
            StructField('w4flg', IntegerType(), True),
            StructField('w4mcor', DoubleType(), True),
            StructField('w1mag_1', DoubleType(), True),
            StructField('w1sigm_1', DoubleType(), True),
            StructField('w1flg_1', IntegerType(), True),
            StructField('w2mag_1', DoubleType(), True),
            StructField('w2sigm_1', DoubleType(), True),
            StructField('w2flg_1', IntegerType(), True),
            StructField('w3mag_1', DoubleType(), True),
            StructField('w3sigm_1', DoubleType(), True),
            StructField('w3flg_1', IntegerType(), True),
            StructField('w4mag_1', DoubleType(), True),
            StructField('w4sigm_1', DoubleType(), True),
            StructField('w4flg_1', IntegerType(), True),
            StructField('w1mag_2', DoubleType(), True),
            StructField('w1sigm_2', DoubleType(), True),
            StructField('w1flg_2', IntegerType(), True),
            StructField('w2mag_2', DoubleType(), True),
            StructField('w2sigm_2', DoubleType(), True),
            StructField('w2flg_2', IntegerType(), True),
            StructField('w3mag_2', DoubleType(), True),
            StructField('w3sigm_2', DoubleType(), True),
            StructField('w3flg_2', IntegerType(), True),
            StructField('w4mag_2', DoubleType(), True),
            StructField('w4sigm_2', DoubleType(), True),
            StructField('w4flg_2', IntegerType(), True),
            StructField('w1mag_3', DoubleType(), True),
            StructField('w1sigm_3', DoubleType(), True),
            StructField('w1flg_3', IntegerType(), True),
            StructField('w2mag_3', DoubleType(), True),
            StructField('w2sigm_3', DoubleType(), True),
            StructField('w2flg_3', IntegerType(), True),
            StructField('w3mag_3', DoubleType(), True),
            StructField('w3sigm_3', DoubleType(), True),
            StructField('w3flg_3', IntegerType(), True),
            StructField('w4mag_3', DoubleType(), True),
            StructField('w4sigm_3', DoubleType(), True),
            StructField('w4flg_3', IntegerType(), True),
            StructField('w1mag_4', DoubleType(), True),
            StructField('w1sigm_4', DoubleType(), True),
            StructField('w1flg_4', IntegerType(), True),
            StructField('w2mag_4', DoubleType(), True),
            StructField('w2sigm_4', DoubleType(), True),
            StructField('w2flg_4', IntegerType(), True),
            StructField('w3mag_4', DoubleType(), True),
            StructField('w3sigm_4', DoubleType(), True),
            StructField('w3flg_4', IntegerType(), True),
            StructField('w4mag_4', DoubleType(), True),
            StructField('w4sigm_4', DoubleType(), True),
            StructField('w4flg_4', IntegerType(), True),
            StructField('w1mag_5', DoubleType(), True),
            StructField('w1sigm_5', DoubleType(), True),
            StructField('w1flg_5', IntegerType(), True),
            StructField('w2mag_5', DoubleType(), True),
            StructField('w2sigm_5', DoubleType(), True),
            StructField('w2flg_5', IntegerType(), True),
            StructField('w3mag_5', DoubleType(), True),
            StructField('w3sigm_5', DoubleType(), True),
            StructField('w3flg_5', IntegerType(), True),
            StructField('w4mag_5', DoubleType(), True),
            StructField('w4sigm_5', DoubleType(), True),
            StructField('w4flg_5', IntegerType(), True),
            StructField('w1mag_6', DoubleType(), True),
            StructField('w1sigm_6', DoubleType(), True),
            StructField('w1flg_6', IntegerType(), True),
            StructField('w2mag_6', DoubleType(), True),
            StructField('w2sigm_6', DoubleType(), True),
            StructField('w2flg_6', IntegerType(), True),
            StructField('w3mag_6', DoubleType(), True),
            StructField('w3sigm_6', DoubleType(), True),
            StructField('w3flg_6', IntegerType(), True),
            StructField('w4mag_6', DoubleType(), True),
            StructField('w4sigm_6', DoubleType(), True),
            StructField('w4flg_6', IntegerType(), True),
            StructField('w1mag_7', DoubleType(), True),
            StructField('w1sigm_7', DoubleType(), True),
            StructField('w1flg_7', IntegerType(), True),
            StructField('w2mag_7', DoubleType(), True),
            StructField('w2sigm_7', DoubleType(), True),
            StructField('w2flg_7', IntegerType(), True),
            StructField('w3mag_7', DoubleType(), True),
            StructField('w3sigm_7', DoubleType(), True),
            StructField('w3flg_7', IntegerType(), True),
            StructField('w4mag_7', DoubleType(), True),
            StructField('w4sigm_7', DoubleType(), True),
            StructField('w4flg_7', IntegerType(), True),
            StructField('w1mag_8', DoubleType(), True),
            StructField('w1sigm_8', DoubleType(), True),
            StructField('w1flg_8', IntegerType(), True),
            StructField('w2mag_8', DoubleType(), True),
            StructField('w2sigm_8', DoubleType(), True),
            StructField('w2flg_8', IntegerType(), True),
            StructField('w3mag_8', DoubleType(), True),
            StructField('w3sigm_8', DoubleType(), True),
            StructField('w3flg_8', IntegerType(), True),
            StructField('w4mag_8', DoubleType(), True),
            StructField('w4sigm_8', DoubleType(), True),
            StructField('w4flg_8', IntegerType(), True),
            StructField('w1magp', DoubleType(), True),
            StructField('w1sigp1', DoubleType(), True),
            StructField('w1sigp2', DoubleType(), True),
            StructField('w1k', DoubleType(), True),
            StructField('w1ndf', IntegerType(), True),
            StructField('w1mlq', DoubleType(), True),
            StructField('w1mjdmin', DoubleType(), True),
            StructField('w1mjdmax', DoubleType(), True),
            StructField('w1mjdmean', DoubleType(), True),
            StructField('w2magp', DoubleType(), True),
            StructField('w2sigp1', DoubleType(), True),
            StructField('w2sigp2', DoubleType(), True),
            StructField('w2k', DoubleType(), True),
            StructField('w2ndf', IntegerType(), True),
            StructField('w2mlq', DoubleType(), True),
            StructField('w2mjdmin', DoubleType(), True),
            StructField('w2mjdmax', DoubleType(), True),
            StructField('w2mjdmean', DoubleType(), True),
            StructField('w3magp', DoubleType(), True),
            StructField('w3sigp1', DoubleType(), True),
            StructField('w3sigp2', DoubleType(), True),
            StructField('w3k', DoubleType(), True),
            StructField('w3ndf', IntegerType(), True),
            StructField('w3mlq', DoubleType(), True),
            StructField('w3mjdmin', DoubleType(), True),
            StructField('w3mjdmax', DoubleType(), True),
            StructField('w3mjdmean', DoubleType(), True),
            StructField('w4magp', DoubleType(), True),
            StructField('w4sigp1', DoubleType(), True),
            StructField('w4sigp2', DoubleType(), True),
            StructField('w4k', DoubleType(), True),
            StructField('w4ndf', IntegerType(), True),
            StructField('w4mlq', DoubleType(), True),
            StructField('w4mjdmin', DoubleType(), True),
            StructField('w4mjdmax', DoubleType(), True),
            StructField('w4mjdmean', DoubleType(), True),
            StructField('rho12', IntegerType(), True),
            StructField('rho23', IntegerType(), True),
            StructField('rho34', IntegerType(), True),
            StructField('q12', IntegerType(), True),
            StructField('q23', IntegerType(), True),
            StructField('q34', IntegerType(), True),
            StructField('xscprox', DoubleType(), True),
            StructField('w1rsemi', DoubleType(), True),
            StructField('w1ba', DoubleType(), True),
            StructField('w1pa', DoubleType(), True),
            StructField('w1gmag', DoubleType(), True),
            StructField('w1gerr', DoubleType(), True),
            StructField('w1gflg', IntegerType(), True),
            StructField('w2rsemi', DoubleType(), True),
            StructField('w2ba', DoubleType(), True),
            StructField('w2pa', DoubleType(), True),
            StructField('w2gmag', DoubleType(), True),
            StructField('w2gerr', DoubleType(), True),
            StructField('w2gflg', IntegerType(), True),
            StructField('w3rsemi', DoubleType(), True),
            StructField('w3ba', DoubleType(), True),
            StructField('w3pa', DoubleType(), True),
            StructField('w3gmag', DoubleType(), True),
            StructField('w3gerr', DoubleType(), True),
            StructField('w3gflg', IntegerType(), True),
            StructField('w4rsemi', DoubleType(), True),
            StructField('w4ba', DoubleType(), True),
            StructField('w4pa', DoubleType(), True),
            StructField('w4gmag', DoubleType(), True),
            StructField('w4gerr', DoubleType(), True),
            StructField('w4gflg', IntegerType(), True),
            StructField('tmass_key', IntegerType(), True),
            StructField('r_2mass', DoubleType(), True),
            StructField('pa_2mass', DoubleType(), True),
            StructField('n_2mass', IntegerType(), True),
            StructField('j_m_2mass', DoubleType(), True),
            StructField('j_msig_2mass', DoubleType(), True),
            StructField('h_m_2mass', DoubleType(), True),
            StructField('h_msig_2mass', DoubleType(), True),
            StructField('k_m_2mass', DoubleType(), True),
            StructField('k_msig_2mass', DoubleType(), True),
            StructField('x', DoubleType(), True),
            StructField('y', DoubleType(), True),
            StructField('z', DoubleType(), True),
            StructField('spt_ind', IntegerType(), True),
            StructField('htm20', LongType(), True),
])

panstarrs_dr1_otmo_schema = StructType([
            StructField('obj_id', LongType(), True),
            StructField('projection_id', ShortType(), True),
            StructField('sky_cell_id', ShortType(), True),
            StructField('obj_info_flag', IntegerType(), True),
            StructField('quality_flag', ShortType(), True),
            StructField('ra_mean', DoubleType(), True),
            StructField('dec_mean', DoubleType(), True),
            StructField('ra_mean_err', FloatType(), True),
            StructField('dec_mean_err', FloatType(), True),
            StructField('epoch_mean', DoubleType(), True),
            StructField('n_stack_detections', ShortType(), True),
            StructField('n_detections', ShortType(), True),
            StructField('ng', ShortType(), True),
            StructField('nr', ShortType(), True),
            StructField('ni', ShortType(), True),
            StructField('nz', ShortType(), True),
            StructField('ny', ShortType(), True),
            StructField('g_qf_perfect', FloatType(), True),
            StructField('g_mean_psf_mag', FloatType(), True),
            StructField('g_mean_psf_mag_err', FloatType(), True),
            StructField('g_mean_psf_mag_std', FloatType(), True),
            StructField('g_mean_psf_mag_npt', ShortType(), True),
            StructField('g_mean_psf_mag_min', FloatType(), True),
            StructField('g_mean_psf_mag_max', FloatType(), True),
            StructField('g_mean_kron_mag', FloatType(), True),
            StructField('g_mean_kron_mag_err', FloatType(), True),
            StructField('g_flags', IntegerType(), True),
            StructField('r_qf_perfect', FloatType(), True),
            StructField('r_mean_psf_mag', FloatType(), True),
            StructField('r_mean_psf_mag_err', FloatType(), True),
            StructField('r_mean_psf_mag_std', FloatType(), True),
            StructField('r_mean_psf_mag_npt', ShortType(), True),
            StructField('r_mean_psf_mag_min', FloatType(), True),
            StructField('r_mean_psf_mag_max', FloatType(), True),
            StructField('r_mean_kron_mag', FloatType(), True),
            StructField('r_mean_kron_mag_err', FloatType(), True),
            StructField('r_flags', IntegerType(), True),
            StructField('i_qf_perfect', FloatType(), True),
            StructField('i_mean_psf_mag', FloatType(), True),
            StructField('i_mean_psf_mag_err', FloatType(), True),
            StructField('i_mean_psf_mag_std', FloatType(), True),
            StructField('i_mean_psf_mag_npt', ShortType(), True),
            StructField('i_mean_psf_mag_min', FloatType(), True),
            StructField('i_mean_psf_mag_max', FloatType(), True),
            StructField('i_mean_kron_mag', FloatType(), True),
            StructField('i_mean_kron_mag_err', FloatType(), True),
            StructField('i_flags', IntegerType(), True),
            StructField('z_qf_perfect', FloatType(), True),
            StructField('z_mean_psf_mag', FloatType(), True),
            StructField('z_mean_psf_mag_err', FloatType(), True),
            StructField('z_mean_psf_mag_std', FloatType(), True),
            StructField('z_mean_psf_mag_npt', ShortType(), True),
            StructField('z_mean_psf_mag_min', FloatType(), True),
            StructField('z_mean_psf_mag_max', FloatType(), True),
            StructField('z_mean_kron_mag', FloatType(), True),
            StructField('z_mean_kron_mag_err', FloatType(), True),
            StructField('z_flags', IntegerType(), True),
            StructField('y_qf_perfect', FloatType(), True),
            StructField('y_mean_psf_mag', FloatType(), True),
            StructField('y_mean_psf_mag_err', FloatType(), True),
            StructField('y_mean_psf_mag_std', FloatType(), True),
            StructField('y_mean_psf_mag_npt', ShortType(), True),
            StructField('y_mean_psf_mag_min', FloatType(), True),
            StructField('y_mean_psf_mag_max', FloatType(), True),
            StructField('y_mean_kron_mag', FloatType(), True),
            StructField('y_mean_kron_mag_err', FloatType(), True),
            StructField('y_flags', IntegerType(), True),
])

# crossmatch table schemas:

# PS1
panstarrs1_best_neighbour_schema = StructType([
            StructField('source_id', LongType(), True),
            StructField('clean_panstarrs1_oid', LongType(), True),
            StructField('original_ext_source_id', LongType(), True),
            StructField('angular_distance', FloatType(), True),
            StructField('number_of_neighbours', ByteType(), True),
            StructField('number_of_mates', ByteType(), True),
            StructField('xm_flag', ShortType(), True),
])

# ALLWISE:
allwise_best_neighbour_schema = StructType([
            StructField('source_id', LongType(), True),
            StructField('original_ext_source_id', StringType(), True),
            StructField('angular_distance', FloatType(), True),
            StructField('xm_flag', ShortType(), True),
            StructField('allwise_oid', IntegerType(), True),
            StructField('number_of_neighbours', ByteType(), True),
            StructField('number_of_mates', ByteType(), True),
])

# 2MASS:
tmasspscxsc_best_neighbour_schema = StructType([
            StructField('source_id', LongType(), True),
            StructField('original_ext_source_id', StringType(), True),
            StructField('angular_distance', FloatType(), True),
            StructField('xm_flag', ShortType(), True),
            StructField('clean_tmass_psc_xsc_oid', IntegerType(), True),
            StructField('number_of_neighbours', ByteType(), True),
            StructField('number_of_mates', ByteType(), True),
])

# base folder for all products of this release
release_folder = 'GEDR3'

# dictionary of all tables: key is table name, value = tuple(tuple of schema(s), subfolder containing parquet files)
table_dict = {
    'gaia_source' : 
        ([gaia_source_schema], release_folder + '/GEDR3_GAIASOURCE'),
    'gaia_source_tmasspsc_best_neighbours' : 
        ([tmasspscxsc_best_neighbour_schema, twomass_psc_schema], release_folder + '/GEDR3_2MASSPSC_BEST_NEIGHBOURS'),
    'gaia_source_allwise_best_neighbours' : 
        ([allwise_best_neighbour_schema, allwise_sc_schema], release_folder + '/GEDR3_ALLWISE_BEST_NEIGHBOURS'),
    'gaia_source_ps1_best_neighbours' : 
        ([panstarrs1_best_neighbour_schema, panstarrs_dr1_otmo_schema], release_folder + '/GEDR3_PS1_BEST_NEIGHBOURS')
}


